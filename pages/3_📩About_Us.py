import streamlit as st
from PIL import Image
import os
from pathlib import Path


st.set_page_config(
    page_title="Fairytalegenerator",
    page_icon="envelope_with_arrow",
)

script_dir = os.path.dirname(__file__)

st.caption("Our Mission")
st.title("Unleashing freedom, empowered by technology.")
st.subheader("科技,释放自由。")
col1, col2 = st.columns(2)

with col1:
    st.caption("Our Story")
    st.write("A diverse team of talented individuals united by their passion for technology embarked on an extraordinary journey, leveraging AI to create groundbreaking web applications that revolutionized industries and left an indelible mark on the digital landscape.")


with col2:
    st.caption("Our Services")
    st.write("We provide cutting-edge AI-powered web app services, revolutionizing businesses with advanced automation, intelligent insights, and seamless user experiences.")

st.caption("Our Team")

#zhaohan
streamlit_zhaohan = Image.open(script_dir+'/../resources/zhaohan.jpg')
tcol1, tcol2, tcol3= st.columns(3)
with tcol1:
    st.image(streamlit_zhaohan,caption='Zhaohan Yan')

with tcol2:
    st.caption("Tech Lead")
    st.info('''
    System Design  
    Infrastructure  
    Backend Development
    ''')
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/zhaohan-yan" style="float:center"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img></a></div>""", unsafe_allow_html=True)
    
with tcol3:
    code = '''
    B.S CS & Mathematics from Rutgers U  
    M.S.E ECE from Johns Hopkins U
    3+ Years in Tech Industry'''
    st.code(code, language='bash')
st.divider()
#wei
streamlit_wei = Image.open(script_dir+'/../resources/wei.jpg')
tcol1, tcol2, tcol3= st.columns(3)
with tcol1:
    code = '''
    B.S Economics & Retail from UW Madison  
    M.Eng ORIE from Cornell U
    3+ Years in Pharmaceutical Industry'''
    st.code(code, language='bash')

with tcol2:
    st.caption("Operations Management")
    st.info('''
    Data Analytics  
    Marketing Research  
    ''')

    st.divider()
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/weichen328" style="float:center"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img></a></div>""", unsafe_allow_html=True)
    
with tcol3:
    st.image(streamlit_wei,caption='Wei Chen')
st.divider()
#mingyang
streamlit_mingyang = Image.open(script_dir+'/../resources/mingyang.jpg')
tcol1, tcol2, tcol3= st.columns(3)
with tcol1:
    st.image(streamlit_mingyang,caption='Mingyang Xiao')

with tcol2:
    st.caption("Project Management")
    st.info('''
    Coordination  
    Organization  
    ''')

    st.divider()
    st.write("""<div style="width:100%;text-align:center;"><a href="https://www.linkedin.com/in/mingyang-xiao-3173a3159" style="float:center"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="22px"></img></a></div>""", unsafe_allow_html=True)
    
with tcol3:
    code = '''
    B.S BAIT from Rutgers U   
    2+ Years in Management Consulting'''
    st.code(code, language='bash')
st.divider()
#woody
streamlit_woody = Image.open(script_dir+'/../resources/woody.jpg')
tcol1, tcol2, tcol3= st.columns(3)
with tcol1:
    code = '''
    2+ Years in Feline Industry'''
    st.code(code, language='bash')

with tcol2:
    st.caption("Chief Feline Officer")
    st.info('''
    Emotional Support  
    Stress Reduction  
    Team Morale Boost
    ''')

    st.divider()

with tcol3:
    st.image(streamlit_woody,caption='Woody')
st.divider()
st.caption("Our Footprint")
mcol1,mcol2, mcol3 = st.columns(3)
with mcol1:
    st.metric(label="Happiness", value="100%", delta="100%")

with mcol2:
    st.metric(label="Creativeness", value="100%", delta="100%")

with mcol3:
    st.metric(label="Stressness", value="0%", delta="-100%")


st.caption("Support Us")
st.write("Enjoying our application?")
st.write(" Your generous donations can contribute to the longevity of our web service, allowing us to continue providing a seamless experience.")

st.write("""<div style="width:100%;text-align:center;"><a href="https://gofund.me/09597477" style="float:center"><img src="https://1000logos.net/wp-content/uploads/2023/01/GoFundMe-Logo-2018.png" width="100px"></img></a></div>""", unsafe_allow_html=True)






