# todo for each directory cnt make a plot
import os
import seaborn as sns
import numpy as np
import pandas as pd
num_classes = 48
import random

def pad(s):
    return "0"*(5-len(s)) + s

def plot_per_freq_class():
    path = os.path.join(os.environ['Bosch'], 'GTSRB', 'Final_Training', 'Images' )
    freq=[]
    for i in range(num_classes):
        #full_path = path + pad(str(i))
        full_path = os.path.join(path, pad(str(i)))
        lst = os.listdir(full_path)
        cnt= 0
        for f in lst:
            if(f.endswith('.ppm') or f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')):
                cnt+=1
        freq.append(cnt)
    
    labels = ["Class"+str(i) for i in range(48)]
    return list(zip(labels,freq))

