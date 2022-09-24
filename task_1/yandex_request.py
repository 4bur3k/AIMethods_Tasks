import base64
import json
from urllib import request
import requests
from area_selection import select_area
# Making POST request to Yandex. 
# Taking 1 argument: image to analys
# Returns array, contains:
# image with selected areas
# count of faces
def request(image_file_name):

    image_file = open(f'./data/{image_file_name}', 'rb')
    
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
    responce_data = response.json()
    
    #writing resoult of the request down
    with open('output.json', 'w') as res_f:
        json.dump(response.json(), res_f)

    #choose left bottom and right top vertices
    detected_faces_vertices = responce_data['results'][0]['results'][0]['faceDetection']['faces'][0]['boundingBox']['vertices']
    vertices_array = list()
    for vertice in detected_faces_vertices[::2]:
        vertices_array.append((int(vertice['x']), int(vertice['y'])))

    chunked_list = list()
    for i in range(0, len(vertices_array), 2):
        chunked_list.append(vertices_array[i:i+2])
    vertices_array = chunked_list
    print(vertices_array)

    faces_count = len(vertices_array)
    print(vertices_array)
    
    resoult_image = select_area(vertices_array, image_file_name)

    return [resoult_image, faces_count]
