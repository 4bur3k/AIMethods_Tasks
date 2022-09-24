import base64
import json
from urllib import request
import requests

#making POST request to Yandex
def yandex_request(image_file):
    
    #encoding to base64 format
    image_b64 = base64.b64encode(image_file.read())

    #getting yandex api token from yandex_tkn.txt
    with open("yandex_tkn.txt", 'r', encoding='utf-8') as token_f:
        API_KEY = token_f.read()
    
    #creating POST request
    data_dict = {"folderId":"b1gb2477drh0ivbugf0p", "analyze_specs": [{"content":image_b64.decode(), "features":[{"type": "FACE_DETECTION"}]}]}

    header = {"Authorization": f"Api-Key {API_KEY}"}

    #doing request
    response = requests.post("https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze", json=data_dict, headers=header)
    print(f'Response code:{response}')
    request_resoult = response.json()
    print(f'Resoult{request_resoult}')

    #writing resoult of the request down
    with open('output.json', 'w') as res_f:
        detected_faces = json.dump(request_resoult, res_f)


