#1
import streamlit as st
import pandas as pd
import numpy as np
import base64
import json

#encoding to base64 format
def encode_file(file):
    file_content = file.read()
    return base64.b64encode(file_content)

#updating body.json
def make_json_body(file):
    base64_file = encode_file(file)
    return {"folderId":"b1gb2477drh0ivbugf0p", "analyze_specs": [{"content":str(base64_file)}, "features":[{"type": "FACE_DETECTION"}]}]}


with open ('./data/mask.jpg', 'rb') as img:
    with open ("body.json", 'w', encoding='utf-8') as json_f:
        res_json = make_json_body(img)
        json.dump(make_json_body(img), json_f)
