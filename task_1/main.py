import yandex_detection
import google_detection
import streamlit as st
from PIL import Image


#for i in range(1,11):
    #yandex_resoult = yandex_detection.detect_faces(f'{i}.jpg')
    #print(f'On {yandex_resoult[0]} detected {yandex_resoult[1]} person')

st.title('Faces recognition')

images = list()
for i in range (1, 11):
    img = Image.open(f'output_yandex/{i}.jpg')
    images.append(img)

st.image(images)
