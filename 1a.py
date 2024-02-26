###############################################################
#Initialization of repository and location
PROJECT_ID = "a-hack-414803"
REGION = "us-central1"
LOCATION = "us-central1"
#BUCKET_URI = "gs://customer_voice_packets"
#account_sid = 'AC0e3733bb6c768c2b621af786e924ce48'
#################################################################

###############################################################################
### Importing python modules
from pathlib import Path as p
#from twilio.rest import Client
import streamlit as st
import glob, os
import PIL.Image
from google.cloud import storage
import google.auth
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.api_core.client_options import ClientOptions
import json
import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.preview.vision_models import ImageGenerationModel
import math
import matplotlib.pyplot as plt
###############################################################################
vertexai.init(project=PROJECT_ID, location=LOCATION)
#client = Client(account_sid, auth_token)
###############################################################################


###############################################################################
def image_creation(image_prompt,file_name):
    if image_prompt!="":
        # prompt = """ You need to strictly restrict images to decorative business like interior design, paints, kitchen products and bathroom products. 
        # Do not generate images for other things. You need to find elements related to decor space in that text and generate images.
        # The message is as follows:"""
        prompt = """You are an interior designing bot with expertise in generating photo-realistic images 
        of living spaces. You are conversant in multiple design language. You are trained on different themes, 
        color schemes, design styles, lighting preferences, and other design elements. 
        """
        prompt = prompt + image_prompt
        generation_model = ImageGenerationModel.from_pretrained("imagegeneration@005")
        response = generation_model.generate_images(
            prompt=prompt,
            number_of_images=4,
        )
        #display_images_in_grid(response.images,file_name)
    else:
        print("Error!")
###############################################################################




import streamlit as st

festival = st.selectbox(
    'Please select festival from the drop down',
    ('Holi', 'Diwali', 'Pongal' , 'Christmas' , 'Ganesh Chaturthi'))

lob = st.selectbox(
    'Please select Line of Business from the drop down',
    ('Kitchen', 'Home Decour', 'Bath' , 'Interior Designs', 'Wallpapers'))

offers = st.selectbox(
    'Please select offer from the drop down',
    ('offer1', 'offer2', 'offer3' , 'offer4' , 'offer5'))

language = st.selectbox(
    'Please select language from the drop down',
    ('Hindi', 'English', 'Tamil' , 'Marathi' , 'Bengali'))

target = st.selectbox(
    'Please select target audiance from the drop down',
    ('Kids', 'Men', 'Women'))

Prompt = st.text_input("Enter additional prompt 👇")

if st.button('Generate'):
    st.title(Prompt)
    PromptForAi = f"Generate a banner for {festival} Festival. The banner should include text specifying {offers} on {lob} in {language}. The banner should include images related to {festival} and {lob} in a collage template."
    print(PromptForAi)
    image_creation(PromptForAi , "temp.jpg")
    
    
