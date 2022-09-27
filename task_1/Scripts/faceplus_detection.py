import base64
import json
import requests
from picrure_conv import select_area, image_distortion

with open('../faceplus_tkn.txt', 'r') as f:
    API_KEY = f.read()

with open('../faceplus_secret.txt', 'r') as f:
    API_SECRET = f.read()

image_path = '../data/man.jpg'

with open(image_path, 'rb') as f:
    image_b64 = base64.b64encode(f.read())

data = {'api_key':API_KEY, 'api_secret':API_SECRET, "image_base64":image_b64}

response = requests.post("https://api-us.faceplusplus.com/facepp/v3/detect", data=data)

print(response, response.reason, response.text)

# with open('test.json', 'r') as f:
#     aDict = json.loads(f.read())

aDict = json.loads(response.text)

newList = list()
verticeList = list()
for vertice in aDict['faces']:
    newList.append(list(vertice['face_rectangle'].values()))

print(newList)
buffer = list()
for item in newList:
    buf = [(item[1], item[0]), (item[1] + item[2], item[0] + item[3])]
    print(buf)
    verticeList.append(buf)

print('vList: ', verticeList, '\n---')

for item in verticeList:
    print(item)

resoult_image = select_area(verticeList, 'man.jpg', False)
