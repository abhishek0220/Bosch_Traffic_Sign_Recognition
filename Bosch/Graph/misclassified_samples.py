import logging
from flask import Flask
import h5py
from tensorflow import keras
import os
from PIL import Image
import cv2
import numpy as np
import pandas as pd
total_classes = 48
height = 64
width = 64
# reconstructed_model = keras.models.load_model('../my_h5_model.h5')
# model_loaded = load_model('/home/arya/Desktop/main/Sem6/inter_iit/code/Bosch_Traffic_Sign_Recognition/my_h5_model.h5')

class print_samples:
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
        # predictions = model.predict(image_data)

        #comment this
        predictions = np.random.randint(total_classes,size=len(image_labels))
        predictions[0] = image_labels[0]
        #this portion

        misclassified = (predictions==image_labels)
        misclassified = np.where(misclassified == False)
        misclassified = misclassified[0]  

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
            final_predictions.append(predictions[index])

        #misclassified contains the indices 

        final_res = dict()
        final_res["images"] = final_images
        final_res["labels"] = final_labels
        final_res["mispredictions"] = final_predictions

        results["message"] = "Returning " + str(num_images) + " misclassified images"
        results["results"] = final_res
        # print(results["results"]["labels"],results["results"]["mispredictions"])
        return results