#1
import streamlit as st
import pandas as pd
import numpy as np
import base64
import json
import requests
 

#encoding to base64 format
def encode_file(file):
    file_content = file.read()
    return base64.b64encode(file_content)

#dumps image to json in format that api need
def make_json_body():
    with open ('./data/mask.jpg', 'rb') as img:
        base64_file = encode_file(img)
        data = {"folderId":"b1gb2477drh0ivbugf0p", "analyze_specs": [{"content":base64_file.decode(), "features":[{"type": "FACE_DETECTION"}]}]}

        return data

#making POST request
f = open("yandex_tkn.txt", 'r', encoding='utf-8')
API_KEY = f.read()

json_f = open ("body.json", 'r')
data = json.dumps(make_json_body())
print(data)
header = {"Authorization": f"Api-Key {API_KEY}"}

response = requests.post("https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze", json=data, headers=header)
print(f'Response code:{response}')
resoult = response.json()
print(resoult)

with open('output.json', 'w') as res_f:
    detected_faces = json.dump(resoult, res_f)


