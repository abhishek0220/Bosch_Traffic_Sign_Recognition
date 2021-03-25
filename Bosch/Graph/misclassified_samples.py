from tensorflow import keras
import os
from PIL import Image
import cv2
import numpy as np

height = 64
width = 64
# reconstructed_model = keras.models.load_model('../my_h5_model.h5')
# model_loaded = load_model('/home/arya/Desktop/main/Sem6/inter_iit/code/Bosch_Traffic_Sign_Recognition/my_h5_model.h5')

model = keras.models.load_model('Bosch/my_h5_model.h5')
class print_samples:
    def brightness_code(val):
        if(val<0.3):
            return 'red'
        elif(val<0.4):
            return 'orange'
        else:
            return 'green'
    
    def contrast_code(val):
        if(val<20 or val>90):
            return 'red'
        elif(val<30 or val>80):
            return 'orange'
        else:
            return 'green'
    

    def sharpness_code(val):
        if(val<10):
            return 'red'
        elif(val<20):
            return 'orange'
        else:
            return 'green'

    def basic(default_class = 0):     #change with user input for class labels

        results=dict()
        input_path = 'Bosch/GTSRB/'
        image_data = []
        image_labels = []
        path = input_path + 'Final_Training/Images/' + (str(default_class).zfill(5))
        images = os.listdir(path)
        for img in images:
            try:
                image = cv2.imread(path + '/' + img)
                image_fromarray = Image.fromarray(image, 'RGB')
                resize_image = image_fromarray.resize((height, width))
                image_data.append(np.array(resize_image))
                image_labels.append(default_class)
            except:
                print("Error - Image loading",path + '/' + img)
        image_data = np.array(image_data)
        image_labels = np.array(image_labels)

        #uncomment this code
        preds = model.predict(image_data)
        predictions=[]
        for p in preds:
            predictions.append(np.argmax(p))
        predictions = np.array(predictions)
        #comment this
        # predictions = np.random.randint(total_classes,size=len(image_labels))
        # predictions[0] = image_labels[0]
        #this portion
        # for i in predictions:
        #     print(i)
        misclassified = (predictions==image_labels)
        misclassified = np.where(misclassified == False)
        misclassified = misclassified[0]  
        #print(misclassified)
        final_images = []
        final_labels = []
        final_predictions = []      

        np.random.shuffle(misclassified)
        num_images = 4
        if (len(misclassified) < 4):
            num_images = len(misclassified)
        for i in range(num_images):
            index = misclassified[i]
            final_images.append(image_data[index])
            final_labels.append(image_labels[index])
            final_predictions.append((predictions[index]))

        #misclassified contains the indices 

        final_res = dict()
        final_res["images"] = final_images
        final_res["labels"] = final_labels
        final_res["mispredictions"] = final_predictions
        print(final_predictions)
        results["message"] = "Returning " + str(num_images) + " misclassified images"
        results["results"] = final_res

        retval=[]
        for i in range(num_images):
            im = Image.fromarray(final_images[i])
            save_path = 'Bosch/static/misclassified'+str(i)+'.png'
            im.save(save_path)
            brightness, contrast, sharpness = print_samples.calc_attributes(save_path)
            b_color, c_color, s_color = print_samples.brightness_code(brightness), print_samples.contrast_code(contrast), print_samples.sharpness_code(sharpness)
            x = {"ImageLoc":save_path, 
                 "correct_label":int(final_labels[i]),
                 "predicted_label":int(final_predictions[i]),
                 "brightness": f"{brightness:.4f}",
                 "contrast" : f"{contrast:.4f}",
                 "sharpness":f"{sharpness:.4f}",
                 "b_color":b_color,
                 "c_color":c_color,
                 "s_color":s_color
            }
            retval.append(x)
        #print(results["results"]["labels"],results["results"]["mispredictions"])
        return retval
    def calc_attributes(save_path):
        im = Image.open(save_path)
        greyscale_image = im.convert('L')
        contrast = np.array(greyscale_image).std()
        array = np.asarray(greyscale_image, dtype=np.int32)

        gy, gx = np.gradient(array)
        gnorm = np.sqrt(gx**2 + gy**2)
        sharpness = np.average(gnorm)
        
        histogram = greyscale_image.histogram()
        pixels = sum(histogram)
        brightness = scale = len(histogram)

        for index in range(0, scale):
            ratio = histogram[index] / pixels
            brightness += ratio * (-scale + index)
        if(brightness == 255):
            brightness = 1
        else:
            brightness = brightness / scale
        return brightness,contrast,sharpness
#test
#print(print_samples.basic(1))
