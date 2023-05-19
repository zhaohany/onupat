import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Fairytalegenerator",
    page_icon="european_castle",
)

def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
       return json.load(f)

script_dir = os.path.dirname(__file__)
tcol1, tcol2 = st.columns(2)
with tcol1:
   landing_img2 = Image.open(script_dir+'/resources/landing2.png')
   st.image(landing_img2)
   lottie_landingwritter = load_lottiefile(script_dir+'/resources/landingwritter.json')
   st_lottie(lottie_landingwritter, speed = 1,loop = True,  key="lottie_landingwritter")
   st.caption("Surrender to Imagination: Delve into AI-Generated Fairy Tales that Captivate and Inspire")

with tcol2:
   st.title("Unlock Enchanting Worlds: Where AI Creates Fairy Tales")
   landing_img1 = Image.open(script_dir+'/resources/landing1.png')
   st.image(landing_img1)

 


video_file = open(script_dir+'/resources/intro.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.caption('Powering Innovations: Unleashing the Technology Behind Our Website')
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
   streamlit_logo = Image.open(script_dir+'/resources/streamlit.png')
   st.image(streamlit_logo)

with col2:
   openai_logo = Image.open(script_dir+'/resources/openai.png')
   st.image(openai_logo)

with col3:
   hugging_face_logo = Image.open(script_dir+'/resources/hugging_face.png')
   st.image(hugging_face_logo)

with col4:
   tensorflow_logo = Image.open(script_dir+'/resources/tensorflow.png')
   st.image(tensorflow_logo)

with col5:
   python_logo = Image.open(script_dir+'/resources/python.png')
   st.image(python_logo)

with col6:
   canva_logo = Image.open(script_dir+'/resources/canva.png')
   st.image(canva_logo)
