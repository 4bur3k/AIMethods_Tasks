from random import choices
import yandex_detection
import google_detection
import streamlit as st
from PIL import Image

ST_PICS_WIDTH = 500
CAMERA_DISABLE_FLAG = True
persons_count = 0

st.title('Face recognition')

with st.sidebar:
    #selectbox with list of avaible pictures
    choise = st.selectbox(
                'Choose picture to detect', 
                ('me', 'brigade', 'day_of_death', 'film', 'meme',  
                'main_in_facemask', 'people_in_facemasks', 'man', 'people', 'students'))


    #select scale number
    scalex = scaley = st.slider("Image scale")

    st.write('or')

    colx, coly = st.columns(2) 
    scalex = colx.number_input('x scale')
    scaley = coly.number_input('y scale')
    

    #uploading tools           
    with st.expander('Uploading tools:'):
        agree = st.checkbox('Enable camera')
        if agree:   CAMERA_DISABLE_FLAG = False
        else :  CAMERA_DISABLE_FLAG = True

        picture = st.camera_input('You can make a photo of yourself', disabled=CAMERA_DISABLE_FLAG)
        picture = st.file_uploader('You can upload your own picture')

    APPLY_BUTTON_PRESSED = st.button('Apply')

if APPLY_BUTTON_PRESSED:
    # if not picture:
    #     img = Image.open(picture)
    #     img.save('data/live.jpg')
    #     choise = 'live'
    # else:
    #     st.image(f'output_yandex/{choise}.jpg', caption=f'{persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)

    yandex_resoult = yandex_detection.detect_faces(f'{choise}.jpg')
    persons_count = yandex_resoult[1]

    st.image(f'output_yandex/{choise}.jpg', caption=f'{persons_count} persons detected in this picture' ,width=ST_PICS_WIDTH)

    APPLY_BUTTON_PRESSED = False
