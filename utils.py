import base64
import io

from PIL import Image


def ouvrirImage(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return data

def base64ToImage(imageBase64):
    imageBytes = base64.b64decode(imageBase64)
    return Image.open(io.BytesIO(imageBytes))