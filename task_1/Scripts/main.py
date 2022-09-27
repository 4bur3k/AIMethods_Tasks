import yandex_detection
import google_detection
import streamlit as st
from PIL import Image


ST_PICS_WIDTH = 500
CAMERA_DISABLE_FLAG = True
persons_count_original = 0
persons_count_distorted = 0

st.title('Face recognition')

#image manipulation menu
with st.sidebar:
    #selectbox with list of avaible pictures
    chosen_picture = st.selectbox(
                'Choose picture to detect', 
                ('me', 'brigade', 'day_of_death', 'film', 'meme',  
                'man_in_facemask', 'people_in_facemasks', 'man', 'people', 'people2', 'people_scaceld', 'students'))


    #select quality value
    image_quality = st.slider("Image quality", max_value=99)
    

    #uploading tools           
    with st.expander('Uploading tools:'):
        agree = st.checkbox('Enable camera')
        if agree:   CAMERA_DISABLE_FLAG = False
        else :  CAMERA_DISABLE_FLAG = True

        picture = st.camera_input('You can make a photo of yourself', disabled=CAMERA_DISABLE_FLAG)
        picture = st.file_uploader('You can upload your own picture')


#show pictures
if picture:
    img = Image.open(picture)
    img.save('../data/live.jpg')
    chosen_picture = 'live'


#detecting faces on original and distorted image
print(f"yandex detection executing  \"{chosen_picture}\"")
yandex_resoult_original = yandex_detection.detect_faces(f'{chosen_picture}.jpg', 100)
persons_count_original = yandex_resoult_original[1]

yandex_resoult_distorted = yandex_detection.detect_faces(f'{chosen_picture}.jpg', image_quality)
persons_count_distorted = yandex_resoult_distorted[1]


print(f"images showing  \"{chosen_picture}\"\n " +
        "------------------------------")
st.image(f'../output_yandex/{chosen_picture}.jpg', caption=f'Original picture. {persons_count_original} persons detected in this picture' ,width=ST_PICS_WIDTH)
st.image(f'../distorted/{chosen_picture}.jpg', caption=f'Distorted picture.{persons_count_distorted} persons detected in this picture' ,width=ST_PICS_WIDTH)
