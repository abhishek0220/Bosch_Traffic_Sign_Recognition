from numpy import loadtxt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
import time
import numpy as np 
import pandas as pd
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
np.random.seed(42)
tf.random.set_seed(42)

def pad(s):
	return "0"*(5-len(s)) + s

def retrieve_data_single_class(class_id):
	image_data = []
	image_labels = []
	height = 64
	width = 64
	channels = 3

	input_path = 'Bosch/GTSRB/'
	path = input_path + 'Final_Training/Images/' + pad(str(class_id))
	images = os.listdir(path)
	for img in images:
		try:
			image = cv2.imread(path + '/' + img)
			image_fromarray = Image.fromarray(image, 'RGB')
			resize_image = image_fromarray.resize((height, width))
			image_data.append(np.array(resize_image))
			image_labels.append(class_id)
		except:
			print("Error - Image loading")

	image_data = np.array(image_data)
	image_labels = np.array(image_labels)

	return image_data, image_labels


def get_confusion_matrix_single_class(class_id):

	model = keras.models.load_model('Bosch/my_h5_model.h5')

	new_image_data, new_image_labels = retrieve_data_single_class(class_id)

	predictions = model.predict(new_image_data)
	ans = []
	for p in predictions:
		ans.append(np.argmax(p))
	image_label_preds = np.array(ans)
	print(image_label_preds)
	print(new_image_labels)
	cf_matrix = confusion_matrix(new_image_labels, image_label_preds).ravel()
	return cf_matrix
	

get_confusion_matrix_single_class(23)