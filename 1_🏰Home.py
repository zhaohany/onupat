import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os
import json
from streamlit_lottie import st_lottie
import pathlib
from bs4 import BeautifulSoup
import shutil

def inject_ga():
    GA_ID = "google_analytics"


    GA_JS = """
      <!-- Google tag (gtag.js) -->
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-RC807JENT2"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-RC807JENT2');
      </script>
    """

    # Insert the script in the head tag of the static template inside your virtual
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID): 
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  
        else:
            shutil.copy(index_path, bck_index)  
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        index_path.write_text(new_html)

inject_ga()

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

 


# video_file = open(script_dir+'/resources/intro.mp4', 'rb')
# video_bytes = video_file.read()
st.video("https://youtu.be/j1ACeDBMZLw")

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
