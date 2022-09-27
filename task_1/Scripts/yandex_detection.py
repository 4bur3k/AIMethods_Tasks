import base64
import json
import requests
from picrure_conv import select_area, image_distortion


# Making POST request to Yandex. 
# Taking 1 argument: image to analys
# Returns array, contains:
# image with selected areas
# count of faces
def detect_faces(image_filename, new_quality):

    image_distortion(image_filename, new_quality, 'yandex')

    image_file = open(f'../output_yandex/{image_filename}', 'rb')
    
    #encoding to base64 format
    image_b64 = base64.b64encode(image_file.read())

    #getting yandex api token from yandex_tkn.txt
    with open("../yandex_tkn.txt", 'r', encoding='utf-8') as key_f:
        API_KEY = key_f.read()
    
    #creating POST request
    request_data_dict = {"folderId":"b1gb2477drh0ivbugf0p", "analyze_specs": [{"content":image_b64.decode(), "features":[{"type": "FACE_DETECTION"}], "mimeType":"image/jpeg"}]}

    request_header = {"Authorization": f"Api-Key {API_KEY}"}

    #doing request
    response = requests.post("https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze", json=request_data_dict, headers=request_header)
    print(response)
    responce_data = response.json()
    
    #writing resoult of the request down
    with open('../output.json', 'w') as res_f:
        json.dump(response.json(), res_f)

    #if no faces detected return original image and 0
    if(responce_data['results'][0]['results'][0]['faceDetection'] == {}):
        if new_quality == 100:
            resoult_image = select_area([], image_file_name, 'yandex')
        else:
            resoult_image = select_area([], image_file_name, 'yandex')

        return [resoult_image, 0] 

    responce_data = responce_data['results'][0]['results'][0]['faceDetection']['faces']

    faces_count = len(responce_data)

    #parsing data from json and choosing left bottom and right top vertices
    detected_faces_vertices_array = list()
    for face in responce_data:
        for vertice in face['boundingBox']['vertices'][::2]:
            detected_faces_vertices_array.append((int(vertice['x']), int(vertice['y'])))

    #separate array of vertices into [faces_count] arrays contains 2 vertices
    chunked_list = list()
    for i in range(0, len(detected_faces_vertices_array), 2):
        chunked_list.append(detected_faces_vertices_array[i:i+2])
        print('chunked List: ', chunked_list)
    detected_faces_vertices_array = chunked_list
    print(detected_faces_vertices_array)
    
    resoult_image = select_area(detected_faces_vertices_array, image_file_name, service_name='yandex')
   

    return [resoult_image, faces_count]
