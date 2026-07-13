import os
from dotenv import load_dotenv
import requests
from PIL import Image
import base64
import io

def appelHuggingFace(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(URL_HUGGINGFACE, headers=headers, data=data)
    return response.json()

def base64ToImage(imageBase64):
    imageBytes = base64.b64decode(imageBase64)
    return Image.open(io.BytesIO(imageBytes))

    

load_dotenv()
URL_HUGGINGFACE = os.getenv("URL_HUGGINGFACE")
TOKEN_HUGGINGFACE = os.getenv("TOKEN_HUGGINGFACE")
CHEMIN_IMAGES = "./top_influenceurs_2024/IMG/"


headers = {"Authorization": f"Bearer {TOKEN_HUGGINGFACE}",
           "Content-Type": "image/png"}


contenu = os.listdir(CHEMIN_IMAGES)
def traiterImage(appelHuggingFace, base64ToImage, CHEMIN_IMAGES, image):
    result = appelHuggingFace(CHEMIN_IMAGES+'/'+image)
    images = []
    for masque in result:
        label = masque['label']
        score = masque['score']
        image = base64ToImage(masque['mask']);
        images.append(image)
    imageCompose = Image.composite(images[1], images[2], images[0])
    imageCompose.show()

for image in contenu:
    traiterImage(appelHuggingFace, base64ToImage, CHEMIN_IMAGES, image)

