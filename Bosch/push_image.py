from PIL import Image
from io import BytesIO
import base64

def pushImage(imageb64,class_name,rotation):
    try:
        im = Image.open(BytesIO(base64.b64decode(imgData)))
        im = im.rotate(rotation)
        im.save("Bosch/test.png")
    except:
        return False
    return True