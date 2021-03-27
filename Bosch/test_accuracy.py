import numpy as np 
import os
import cv2
from PIL import Image
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import accuracy_score
import seaborn as sns
import json
np.random.seed(42)
tf.random.set_seed(42)


def test_accuracy1():
    def pad(s):
        return "0"*(5-len(s))+s
    image_data = []
    height = 64
    width = 64
    channels = 3
    input_path = 'Bosch/GTSRB_test/Final_Test/Images'
    test_images = os.listdir(input_path)
    for i in range(len(test_images)):
            try:
                image = cv2.imread(input_path + '/' + pad(str(i))+'.ppm')
                image_fromarray = Image.fromarray(image, 'RGB')
                resize_image = image_fromarray.resize((height, width))
                image_data.append(np.array(resize_image))
            except:
                print("Error - Image loading")

    #Converting lists into numpy arrays
    image_data = np.array(image_data)


    print(image_data.shape)

    model = keras.models.load_model('Bosch/my_h5_model.h5')
    predictions = model.predict(image_data)

    actual = pd.read_csv('Bosch/GTSRB_test/GT-final_test.csv',delimiter=";")
    print(actual.columns)
    actual= actual['ClassId'].values

    actual = np.array(actual)

    ans = []
    for p in predictions:
        ans.append(np.argmax(p))
    ans =np.array(ans)

    test_accuracy = accuracy_score(actual, ans)
    accuracy_coords = {"accuracy":test_accuracy}
    with open('Bosch/static/test_accuracy.json', 'w') as fp:
	    json.dump(accuracy_coords, fp, indent=4)

#test_accuracy1()

    