import yandex_detection
import google_detection
import faceplus_detection
import streamlit as st
from PIL import Image


ST_PICS_WIDTH = 500
CAMERA_DISABLE_FLAG = True
persons_count_original = 0
persons_count_distorted = 0

st.title('Let\'s try to recognize faces')

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


#creating columns for pictures:
col1, col2, col3 = st.columns(3, gap='large')

with col1:
    with st.container():
        st.subheader('Cloud Vision by Yandex')
        #yandex_detecting block[Start]
        #detecting faces on original image
        print(f"Yandex detection executing  \"{chosen_picture}\"")
        yandex_resoult = yandex_detection.detect_faces(f'{chosen_picture}.jpg', 100)
        persons_count = yandex_resoult[1]
        st.image(f'../output_yandex/{chosen_picture}.jpg', caption=f'Original picture. {persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)


        #detecting faces on distorted image
        yandex_resoult = yandex_detection.detect_faces(f'{chosen_picture}.jpg', image_quality)
        persons_count = yandex_resoult[1]
        st.image(f'../output_yandex/{chosen_picture}.jpg', caption=f'Distorted picture.{persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)
        #Yandex detecting block [END]


with col3:
    with st.container():
        st.subheader('Face++ by Megvii')
        #faceplus_detection block[Start]
        #detecting faces on original image
        print(f"faceplus detection executing  \"{chosen_picture}\"")
        faceplus_resoult = faceplus_detection.detect_faces(f'{chosen_picture}.jpg', 100)
        persons_count = faceplus_resoult[1]
        st.image(f'../output_faceplus/{chosen_picture}.jpg', caption=f'Original picture. {persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)
        
        #detecting faces on distorted image
        faceplus_resoult = faceplus_detection.detect_faces(f'{chosen_picture}.jpg', image_quality)
        persons_count = faceplus_resoult[1]
        st.image(f'../output_faceplus/{chosen_picture}.jpg', caption=f'Original picture. {persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)
        #Yandex detecting block [END]


print(f"images showing  \"{chosen_picture}\"\n " +
        "------------------------------")

st.write("Made by Denis Kuznetsov")
