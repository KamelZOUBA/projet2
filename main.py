import os
from dotenv import load_dotenv
import requests

load_dotenv()

URL_HUGGINGFACE = os.getenv("URL_HUGGINGFACE")

TOKEN_HUGGINGFACE = os.getenv("TOKEN_HUGGINGFACE")



headers = {"Authorization": f"Bearer {TOKEN_HUGGINGFACE}",
           "Content-Type": "image/png"}

def appelHuggingFace(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(URL_HUGGINGFACE, headers=headers, data=data)
    return response.json()

result = appelHuggingFace("./top_influenceurs_2024/IMG/image_0.png")
print(result)
