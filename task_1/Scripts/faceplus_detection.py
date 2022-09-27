import base64
import json
from tkinter.tix import FileSelectBox
import requests
from picrure_conv import select_area, image_distortion

with open('../faceplus_tkn.txt', 'r') as f:
    API_KEY = f.read()

with open('../faceplus_secret.txt', 'r') as f:
    API_SECRET = f.read()

image_path = '../data/me.jpg'

with open(image_path, 'rb') as f:
    image_b64 = base64.b64encode(f.read())

data = {'api_key':API_KEY, 'api_secret':API_SECRET, "image_base64":image_b64}
files = {"image_base64":image_b64}

response = requests.post("https://api-us.faceplusplus.com/facepp/v3/detect", data=data)

print(response, response.reason, response.text)