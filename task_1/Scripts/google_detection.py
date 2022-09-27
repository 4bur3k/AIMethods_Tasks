# from email.mime import image
# from http import client
# from google.cloud import vision
# import io
# import os

# def detect_faces(image_file_name):

#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".\symmetric-sonar-341812-c40ad8bd4390.json"
    
#     client = vision.ImageAnnotatorClient()

#     with io.open(f'./data/{image_file_name}', 'rb') as image_file:
#         content = image_file.read()

#     image = vision.Image(content=content)

#     response = client.face_detection(image = image)
#     faces = response.face_annotations

#     likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                        'LIKELY', 'VERY_LIKELY')
#     print('Faces:')

#     for face in faces:
#         print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#         print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
#         print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in face.bounding_poly.vertices])

#         print('face bounds: {}'.format(','.join(vertices)))

#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))
