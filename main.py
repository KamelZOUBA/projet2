import os
from dotenv import load_dotenv
import requests
from PIL import Image
from labels import LABELS_INFO
from utils import base64ToImage, ouvrirImage

def appelHuggingFace(image_path):
    TOKEN_HUGGINGFACE = os.getenv("TOKEN_HUGGINGFACE")
    headers = {"Authorization": f"Bearer {TOKEN_HUGGINGFACE}",
           "Content-Type": "image/png"}
    data = ouvrirImage(image_path)
    response = requests.post(URL_HUGGINGFACE, headers=headers, data=data)
    return response.json()


def traiterImage(i, image):
    result = appelHuggingFace(CHEMIN_IMAGES+'/'+image)
    for index, segment in enumerate(result):
        label = LABELS_INFO[segment['label']]
        imageResultat = base64ToImage(segment['mask']);
        if(index == 0):
            imageCompose = Image.new("RGBA", imageResultat.size, (0, 0, 0, 0))
        coucheCouleur = Image.new("RGBA", imageResultat.size, label['couleur'])
        imageCompose = Image.composite(coucheCouleur, imageCompose, imageResultat)
    imageCompose.show()
    

load_dotenv()
URL_HUGGINGFACE = os.getenv("URL_HUGGINGFACE")
CHEMIN_IMAGES = './top_influenceurs_2024/IMG/'
imagesInitiales = os.listdir(CHEMIN_IMAGES)

for i, image in enumerate(imagesInitiales):
    traiterImage(i, image)

