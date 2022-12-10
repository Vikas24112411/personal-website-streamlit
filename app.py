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

# ---- HEADER SECTION ----
# with st.container():
#     st.subheader("Hi, I am Kruthi :wave:")
#     st.title("A Bio-Informatics Enthusiast")
#     st.subheader("Little about me")
#     st.write(
#         """Post Graduate in  Bioinformatics with work  experience as a Founder. Seeking a challenging role with an organization where I can use my academic knowledge to enhance my learning skills for the mutual growth of the company and myself, willing to give my best. Have a good sense of responsibility, committed, hardworking and can easily adapt the changing situations at work place
#         """
#     )
    # st.write("[Learn More >](https://pythonandvba.com)")

# # ---- WHAT I DO ----
# with st.container():
#     st.write("---")
    # left_column, right_column = st.columns(2)
    # with left_column:
    #     st.header("What I do")
    #     st.write("##")
    #     st.write(
    #         """
    #         On my YouTube channel I am creating tutorials for people who:
    #         - are looking for a way to leverage the power of Python in their day-to-day work.
    #         - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
    #         - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
    #         - are working with Excel and found themselves thinking - "there has to be a better way."
    #
    #         If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
    #         """
    #     )
    #     st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    # with right_column:
    #     st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
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
    # with t1:
    #     with st.container():
    #         st.subheader("Hi, I am Kruthi :wave:")
    #         st.title("A Bio-Informatics Enthusiast")
    #         st.subheader("Little about me")
    #         st.write(
    #             """Post Graduate in  Bioinformatics with work  experience as a Founder. Seeking a challenging role with an organization where I can use my academic knowledge to enhance my learning skills for the mutual growth of the company and myself, willing to give my best. Have a good sense of responsibility, committed, hardworking and can easily adapt the changing situations at work place
    #             """
    #         )
    # with t2:
    #     st.image(img_contact_form)
    t3,t4 = text_column = st.columns((1, 10))
    with t3:
        st.markdown("[LinkedIn...](https://www.linkedin.com/in/inspirekruthirao93939393/)")
    with t4:
        st.markdown("[Instagram...](https://www.instagram.com/_kruthi_rao/)")
    # image_column, text_column = st.columns((1, 5))
    # with image_column:
    #
    #     st.image(img_contact_form)
        # st.markdown()
        # st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png)](http://google.com.au/)")
        # u = """
        #  <img src="/home/rathkanti.s/personal/nithya/personal-website-streamlit/images/nithya.png" alt="Avatar">
        #                 """
        # st.markdown(u, unsafe_allow_html=True)



# # ---- CONTACT ----
# with st.container():
#     st.write("---")
#     st.header("Get In Touch With Me!")
#     st.write("##")
#
#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required>
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()
