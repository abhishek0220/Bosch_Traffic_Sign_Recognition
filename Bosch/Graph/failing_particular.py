import logging
from flask import Flask
import h5py
from tensorflow import keras
import os
from PIL import Image
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.measure import compare_ssim as ssim
total_classes = 48
height = 64
width = 64

rows = 1
columns = 2

class show_SIFT_features():

    def SIFT_compare(misclassified_class=5,input_path='Bosch/Graph/misclassified.jpeg'):

        #fig=plt.figure("Comparing the image")

        #input_path = 'Bosch/Graph/misclassified.jpeg'
        save_path = os.path.join('Bosch', 'static')
        image = cv2.imread(input_path)
        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #keypoints
        sift = cv2.xfeatures2d.SIFT_create(nfeatures=50)
        keypoints_1, descriptors_1 = sift.detectAndCompute(image,None)

        #fig.add_subplot(rows, columns, 1)
        img_1 = cv2.drawKeypoints(gray1,keypoints_1,image)
        Image.fromarray(img_1).save(save_path+"/"+"ms_clsfd.png")
        # plt.imshow(img_1)
        # plt.axis('off')
        # plt.title("First")

        path = 'Bosch/GTSRB/Final_Training/Images/' + (str(misclassified_class).zfill(5))
        images = os.listdir(path)

        s = -1
        final_path2  = ''
        for com_img in images:
            try:
                # print(path + '/' + com_img)
                image_compare = cv2.imread(path + '/' + com_img)
                resize_image = cv2.resize(image_compare, (width,height), interpolation = cv2.INTER_AREA)
                ssim_image1 = cv2.resize(image, (width,height), interpolation = cv2.INTER_AREA)
                ssim_image2 = resize_image 
                # print(ssim_image1.shape,ssim_image1.shape)

                s_curr = ssim(ssim_image1,ssim_image2,multichannel=True)
                if(s_curr>s):
                    s = s_curr
                    final_path2 = com_img
            except:
                print("Error loading",path+'/'+com_img)
            
        # plt.suptitle("Structural similarity : %.2f" % (s))

        image_compare = cv2.imread(path + '/' + com_img)
        resize_image = cv2.resize(image_compare, (width,height), interpolation = cv2.INTER_AREA)        
        gray2 = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
        sift2 = cv2.xfeatures2d.SIFT_create()
        keypoints_2, descriptors_2 = sift2.detectAndCompute(image_compare,None)

        # fig.add_subplot(rows, columns, 2)
        img_2 = cv2.drawKeypoints(gray2,keypoints_2,image_compare)
        Image.fromarray(img_2).save(save_path+"/"+"ms_clsfd_for.png")
        # plt.imshow(img_2);
        # plt.axis('off')
        # plt.title("Second")    

        # fig.savefig(save_path)

        #save the image at this path
        return {"Misclassified_Image":save_path+"/"+"ms_clsfd.png", "Misclassified_for":save_path+"/"+"ms_clsfd_for.png"}
