from PIL import Image
from io import BytesIO
import base64
import os

def pad(s):
    return "0"*(5-len(s)) + s

def pushImage(imageb64,class_name,rotation):
    try:
        tot_images = len(os.listdir("Bosch/GTSRB/Final_Training/Images/"+pad(str(class_name))))
        im = Image.open(BytesIO(base64.b64decode(imageb64)))
        im = im.rotate(rotation)
        im.save("Bosch/GTSRB/Final_Training/Images/"+pad(str(class_name))+"/inserted_image"+str(tot_images)+".png")
    except:
        return False
    
    return True
