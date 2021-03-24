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
import seaborn as sns
np.random.seed(42)
tf.random.set_seed(42)

def retrieve_data_single_class(class_id):
	return "0"*(5-len(s))+s
	image_data = []
	image_labels = []
	height = 32
	width = 32
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

	shuffle_indexes = np.arange(image_data.shape[0])
	np.random.shuffle(shuffle_indexes)
	image_data = image_data[shuffle_indexes]
	image_labels = image_labels[shuffle_indexes]

	return image_data, image_labels


def get_confusion_matrix_single_class(class_id):

	model = load_model('my_h5_model.h5')

	new_image_data, new_image_labels = retrieve_data_single_class(class_id)

	predictions = model.predict(image_data)
	ans = []
	for p in predictions:
		ans.append(np.argmax(p))
	image_label_preds = np.array(ans)

	cf_matrix = confusion_matrix(new_image_labels, image_label_preds)

	group_names = [‘True Neg’,’False Pos’,’False Neg’,’True Pos’]
	group_counts = [“{0:0.0f}”.format(value) for value in cf_matrix.flatten()]
	group_percentages = [“{0:.2%}”.format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
	labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    plt.figure(figsize = (10,7))
	sns_plot = sns.heatmap(cf_matrix, annot = labels, fmt=‘’, cmap='Blues')
	results_path = 'Bosch/static/confusion_matrix_' + pad(str(class_id)) + '.png'
    plt.savefig(results_path, dpi=400)