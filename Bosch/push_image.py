from PIL import Image
from io import BytesIO
import base64

def PushImage(imageb64,class_name,rotation):
    im = Image.open(BytesIO(base64.b64decode(imgData)))
    im = im.rotate(rotation)
    im.save("Bosch/test.png")