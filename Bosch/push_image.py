from PIL import Image
from io import BytesIO
import base64

def pushImage(imageb64,class_name,rotation):
    try:
        im = Image.open(BytesIO(base64.b64decode(imageb64)))
        im = im.rotate(rotation)
        im.save("Bosch/static/test.png")
    except:
        return False
    return True