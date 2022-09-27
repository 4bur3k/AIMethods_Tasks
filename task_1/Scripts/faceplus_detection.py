import base64
import json
from urllib import request
import requests
from picrure_conv import select_area, image_distortion

def detect_faces(image_filename, new_quality):

    image_distortion(image_filename, new_quality, 'faceplus')
    
    with open('../faceplus_tkn.txt', 'r') as f:
        API_KEY = f.read()

    with open('../faceplus_secret.txt', 'r') as f:
        API_SECRET = f.read()

    with open(f'../data/{image_filename}', 'rb') as f:
        image_b64 = base64.b64encode(f.read())

    request_data = {'api_key':API_KEY, 'api_secret':API_SECRET, "image_base64":image_b64}

    response = requests.post("https://api-us.faceplusplus.com/facepp/v3/detect", data=request_data)

    response_data_dict = json.loads(response.text)

    faces_count = response_data_dict['face_num']

    faces_data_array = list()
    for vertice in response_data_dict['faces']:
        faces_data_array.append(list(vertice['face_rectangle'].values()))

    
    vertices_list = list()
    for coordinate in faces_data_array:
        coordinate_buffer = [(coordinate[1], coordinate[0]), (coordinate[1] + coordinate[2], coordinate[0] + coordinate[3])]
        print(coordinate_buffer)
        vertices_list.append(coordinate_buffer)

    print('vList: ', vertices_list, '\n---')

    for item in vertices_list:
        print(item)

    resoult_image = select_area(vertices_list, image_filename, 'faceplus')

    return [resoult_image, faces_count]
