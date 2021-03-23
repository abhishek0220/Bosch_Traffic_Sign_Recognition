import time
import numpy as np
import pandas as pd
import os
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
np.random.seed(42)


def load_and_preprocess():
    start = time.time()
    image_data = []
    image_labels = []
    total_classes = 48
    height = 64
    width = 64
    channels = 3
    input_path = 'Bosch/GTSRB/'
    counter = 0
    for i in range(total_classes):
        if(len(str(i)) == 1):
            path = input_path + 'Final_Training/Images/0000' + str(i)
        else:
            path = input_path + 'Final_Training/Images/000' + str(i)
        print(path)
        images = os.listdir(path)

        for img in images:
            try:
                image = cv2.imread(path + '/' + img)
                image_fromarray = Image.fromarray(image, 'RGB')
                resize_image = image_fromarray.resize((height, width))
                image_data.append(np.array(resize_image))
                image_labels.append(i)
                # counter += 1
            except:
                print("Error - Image loading")

    # Converting lists into numpy arrays
    # print(counter)
    image_data = np.array(image_data)
    image_labels = np.array(image_labels)

    print(image_data.shape, image_labels.shape)
    end = time.time()
    print("It has taken", round(end-start, 5), "seconds")

    shuffle_indexes = np.arange(image_data.shape[0])
    np.random.shuffle(shuffle_indexes)
    image_data = image_data[shuffle_indexes]
    image_labels = image_labels[shuffle_indexes]

    return image_data, image_labels


def train_valid_splitting(image_data, image_labels):
    X_train, X_valid, y_train, y_valid = train_test_split(image_data, image_labels, test_size=0.2, random_state=42, shuffle=True)


    X_train = X_train/255
    X_valid = X_valid/255

    y_train = keras.utils.to_categorical(y_train, total_classes)
    y_valid = keras.utils.to_categorical(y_valid, total_classes)

    return X_train,X_valid,y_train,y_valid
