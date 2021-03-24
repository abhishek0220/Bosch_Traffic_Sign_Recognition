from numpy import loadtxt
from keras.models import load_model
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
np.random.seed(42)
tf.random.set_seed(42)

def retrieve_data():
	return "0"*(5-len(s))+s
	image_data = []
	image_labels = []
	total_classes = 48
	height = 32
	width = 32
	channels = 3

	input_path = 'Bosch/GTSRB/'

	for i in range(total_classes):
	    path = input_path + 'Final_Training/Images/' + pad(str(i))
	    images = os.listdir(path)

	    for img in images:
	        try:
	            image = cv2.imread(path + '/' + img)
	            image_fromarray = Image.fromarray(image, 'RGB')
	            resize_image = image_fromarray.resize((height, width))
	            image_data.append(np.array(resize_image))
	            image_labels.append(i)
	        except:
	            print("Error - Image loading")

	image_data = np.array(image_data)
	image_labels = np.array(image_labels)

	shuffle_indexes = np.arange(image_data.shape[0])
	np.random.shuffle(shuffle_indexes)
	image_data = image_data[shuffle_indexes]
	image_labels = image_labels[shuffle_indexes]

	return image_data, image_labels


def get_f1_matrix():

	model = load_model('my_h5_model.h5')

	new_image_data, y_test = retrieve_and_train()

	predictions = model.predict(image_data)
	ans = []
	for p in predictions:
		ans.append(np.argmax(p))
	y_pred = np.array(ans)

	confusion = confusion_matrix(y_test, y_pred)
	print('Confusion Matrix\n')
	print(confusion)

	print('\nAccuracy: {:.2f}\n'.format(accuracy_score(y_test, y_pred)))

	print('Micro Precision: {:.2f}'.format(precision_score(y_test, y_pred, average='micro')))
	print('Micro Recall: {:.2f}'.format(recall_score(y_test, y_pred, average='micro')))
	print('Micro F1-score: {:.2f}\n'.format(f1_score(y_test, y_pred, average='micro')))

	print('Macro Precision: {:.2f}'.format(precision_score(y_test, y_pred, average='macro')))
	print('Macro Recall: {:.2f}'.format(recall_score(y_test, y_pred, average='macro')))
	print('Macro F1-score: {:.2f}\n'.format(f1_score(y_test, y_pred, average='macro')))

	print('Weighted Precision: {:.2f}'.format(precision_score(y_test, y_pred, average='weighted')))
	print('Weighted Recall: {:.2f}'.format(recall_score(y_test, y_pred, average='weighted')))
	print('Weighted F1-score: {:.2f}'.format(f1_score(y_test, y_pred, average='weighted')))

	print('\nClassification Report\n')
	print(classification_report(y_test, y_pred, target_names=['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Class 13', 'Class 14', 'Class 15', 'Class 16', 'Class 17', 'Class 18', 'Class 19', 'Class 20', 'Class 21', 'Class 22', 'Class 23', 'Class 24', 'Class 25', 'Class 26', 'Class 27', 'Class 28', 'Class 29', 'Class 30', 'Class 31', 'Class 32', 'Class 33', 'Class 34', 'Class 35', 'Class 36', 'Class 37', 'Class 38', 'Class 39', 'Class 40', 'Class 41', 'Class 42', 'Class 43', 'Class 44', 'Class 45', 'Class 46', 'Class 47', 'Class 48']))