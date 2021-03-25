from numpy import loadtxt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np 
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

import json


def pad(s):
	return "0"*(5-len(s))+s

def retrieve_data():
	image_data = []
	image_labels = []
	total_classes = 48
	height = 64
	width = 64
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

	return image_data, image_labels


def get_f1_matrix():

	model = keras.models.load_model('Bosch/my_h5_model.h5')

	new_image_data, y_test = retrieve_data()

	predictions = model.predict(new_image_data)
	ans = []
	for p in predictions:
		ans.append(np.argmax(p))
	y_pred = np.array(ans)

	confusion = confusion_matrix(y_test, y_pred)
	
	report = (classification_report(y_test, y_pred, target_names=['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Class 13', 'Class 14', 'Class 15', 'Class 16', 'Class 17', 'Class 18', 'Class 19', 'Class 20', 'Class 21', 'Class 22', 'Class 23', 'Class 24', 'Class 25', 'Class 26', 'Class 27', 'Class 28', 'Class 29', 'Class 30', 'Class 31', 'Class 32', 'Class 33', 'Class 34', 'Class 35', 'Class 36', 'Class 37', 'Class 38', 'Class 39', 'Class 40', 'Class 41', 'Class 42', 'Class 43', 'Class 44', 'Class 45', 'Class 46', 'Class 47', 'Class 48'], output_dict=True))
	precision=[]
	recall=[]
	f1_score=[]
	for i in range(1,49):
		label = "Class "+str(i)
		dummy = { "y":report[label]["precision"],
				 "label":label }
		precision.append(dummy)

		dummy = { "y":report[label]["recall"],
				 "label":label }
		recall.append(dummy)

		dummy = { "y":report[label]["f1-score"],
				 "label":label }
		f1_score.append(dummy)
	
	precision_coords={"coords":precision, "title":"Precison per class"}
	recall_coords = {"coords":recall, "title":"Recall per class"}
	f1_score_coords={"coords":f1_score, "title":"F1-score per class"}
	accuracy_coords={"accuracy":report["accuracy"]}

	with open('Bosch/static/accuracy.json', 'w') as fp:
		json.dump(accuracy_coords, fp, indent=4)
	
	with open('Bosch/static/precision.json', 'w') as fp:
		json.dump(precision_coords, fp, indent=4)

	with open('Bosch/static/recall.json', 'w') as fp:
		json.dump(recall_coords, fp, indent=4) 
	
	with open('Bosch/static/f1_score.json', 'w') as fp:
		json.dump(f1_score_coords, fp, indent=4)


#(get_f1_matrix())