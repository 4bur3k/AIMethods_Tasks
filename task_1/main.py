from random import choices
import yandex_detection
import google_detection
import streamlit as st
from PIL import Image

ST_PICS_WIDTH = 500
CAMERA_DISABLE_FLAG = True
persons_count_original = 0
persons_count_distorted = 0

st.title('Face recognition')

with st.sidebar:
    #selectbox with list of avaible pictures
    choise = st.selectbox(
                'Choose picture to detect', 
                ('me', 'brigade', 'day_of_death', 'film', 'meme',  
                'man_in_facemask', 'people_in_facemasks', 'man', 'people', 'people_scaceld', 'students'))


    #select scale number
    image_quality = st.slider("Image quality", max_value=99)
    

    #uploading tools           
    with st.expander('Uploading tools:'):
        agree = st.checkbox('Enable camera')
        if agree:   CAMERA_DISABLE_FLAG = False
        else :  CAMERA_DISABLE_FLAG = True

        picture = st.camera_input('You can make a photo of yourself', disabled=CAMERA_DISABLE_FLAG)
        picture = st.file_uploader('You can upload your own picture')

#detecting faces on original and distorted image
yandex_resoult_original = yandex_detection.detect_faces(f'{choise}.jpg', 100)
persons_count_original = yandex_resoult_original[1]

yandex_resoult_distorted = yandex_detection.detect_faces(f'{choise}.jpg', image_quality)
persons_count_distorted = yandex_resoult_distorted[1]

#show pictures
if picture:
    img = Image.open(picture)
    img.save('data/live.jpg')
    choise = 'live'
else:
    st.image(f'output_yandex/{choise}.jpg', caption=f'Distorted picture. {persons_count_distorted} persons detected in this picture' ,width=ST_PICS_WIDTH)
    st.image(f'distorted/{choise}.jpg', caption=f'Original picture.{persons_count_original} persons detected in this picture' ,width=ST_PICS_WIDTH)

