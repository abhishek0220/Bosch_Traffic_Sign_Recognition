import random
import os
from PIL import Image


## use the plotImages function with args as the class you want to initialize
## the image grid will be generated under static with name as random_{classLabel}

image_to_display = 25
def pad(s):
    return "0"*(5-len(s)) + s

def plotImages(classLabel):
    path = os.path.join(os.environ['Bosch'], 'GTSRB', 'Final_Training', 'Images' )
    full_path = os.path.join(path, pad(str(classLabel)))
    multipleImages = os.listdir(full_path)
    filterdImages=[]

    for f in multipleImages:
        if(f.endswith('.ppm') or f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')):
            filterdImages.append(f)
    
    r = random.sample(filterdImages, image_to_display)
    new_im = Image.new('RGB', (125,125))
    idx  = 0
    for i in range(0,125,25):
        for j in range(0,125,25):
            im = Image.open(full_path+"/"+r[idx])
            im.thumbnail((25,25))
            new_im.paste(im, (i,j))
            idx += 1
    new_im.save("Bosch/static/random_visualizer"+str(classLabel)+".png")

#plotImages(47)
    


