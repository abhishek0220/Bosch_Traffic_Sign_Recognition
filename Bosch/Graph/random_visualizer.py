import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random
import cv2
import os


## use the plotImages function with args as the class you want to initialize
## the image grid will be generated under static with name as random_{classLabel}

image_to_display = 16
def pad(s):
    return "0"*(5-len(s)) + s

def plotImages(classLabel):
    path = os.path.join('Bosch', 'GTSRB', 'Final_Training', 'Images' )
    full_path = os.path.join(path, pad(str(classLabel)))
    multipleImages = os.listdir(full_path)
    filterdImages=[]

    for f in multipleImages:
        if(f.endswith('.ppm') or f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')):
            filterdImages.append(f)
    
    r = random.sample(filterdImages, image_to_display)
    plt.figure(figsize=(20,20),facecolor='black',frameon=False)
    plt.subplots_adjust(wspace=0, hspace=0) 
    for i in range(image_to_display):
        plt.subplot(int(image_to_display**0.5),int(image_to_display**0.5),i+1)
        im = cv2.imread(full_path+"/"+r[i])
        plt.imshow(im); plt.axis('off')
    save_path = os.path.join('Bosch', 'static', 'random_'+str(classLabel)+'.png' )
    plt.savefig(save_path)
    return save_path
    


