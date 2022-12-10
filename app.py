import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import urllib.request
from PIL import Image



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
urllib.request.urlretrieve(
  'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
   "gfg.png")
img_contact_form = Image.open("images/nithya2.png").resize((160, 160))
image2 = Image.open("images/yt_lottie_animation.png")
img_lottie_animation = image2.resize((100, 100))

with st.container():
    t1, t2 = st.columns((2,2))
    with t1:
        st.subheader("Hi, I am Kruthi :wave:")
        st.title("A Bio-Informatics Enthusiast")
    with t2:
        st.image(img_contact_form)

    with st.container():
        st.subheader("Little about me")
        st.write("""Post Graduate in  Bioinformatics with work  experience as a Founder. Seeking a challenging role with an organization where I can use my academic knowledge to enhance my learning skills for the mutual growth of the company and myself, willing to give my best. Have a good sense of responsibility, committed, hardworking and can easily adapt the changing situations at work place
                    """
                )
    t3,t4 = text_column = st.columns((1, 10))
    with t3:
        st.markdown("[LinkedIn...](https://www.linkedin.com/in/inspirekruthirao93939393/)")
    with t4:
        st.markdown("[Instagram...](https://www.instagram.com/_kruthi_rao/)")
