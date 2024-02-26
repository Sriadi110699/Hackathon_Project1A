#################################################################
PROJECT_ID = "a-hack-414803"
LOCATION = "us-central1" #e.g. us-central1
REGION = "us-central1"
##################################################################
import streamlit as st
import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)
from vertexai.generative_models import GenerativeModel
from PIL import Image, ImageDraw, ImageFont
import textwrap
from vertexai.preview.vision_models import ImageGenerationModel
generation_model = ImageGenerationModel.from_pretrained("imagegeneration@005")
from vertexai.language_models import TextGenerationModel
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
from PIL import ImageFont
import uuid 
###################################################################################
def text_gen(festival,lob,offer):
    model = GenerativeModel("gemini-1.0-pro")
    message = ""
    prompt = f"You are an expert media content writer. Write content for a image.Create an offer related text which gives message that it is {offer} percent off for a specific {lob} products purchase.It should be a one liner message and eye catching. Wish users a very happy {festival}. The output should be in a plain text. No emojis"

    responses = model.generate_content(prompt, stream=True)
 
    for response in responses:

        message = response.text

        #print(response.text, end="")

    text = textwrap.fill(text=message, width=35)

    return text
###########################################################################333
def lang_trans(festival,lob,offer,basic_text,lang):

    parameters = {

        "candidate_count": 1,

        "max_output_tokens": 1024,

        "temperature": 0.9,

        "top_p": 1 

    }

    model = TextGenerationModel.from_pretrained("text-bison")

    prompt = f"You are an expert language translator. The output should be a plain text. No emojis. Restrict it to 5 words. Convert the text {basic_text} to {lang}:"

    response = model.predict(

        prompt,

        **parameters

    )

    #print(response)

    message = response.text

    #text = textwrap.fill(text=message, width=35)

    return message
###############################################################################################
def display_images_in_grid(images,basic_text,lang_resp):

    # Determine the number of rows and columns for the grid layout.

    nrows = math.ceil(len(images) / 4)  # Display at most 4 images per row

    ncols = min(len(images) + 1, 4)  # Adjust columns based on the number of images

    print(basic_text)

    print(lang_resp)

    # Create a figure and axes for the grid layout.

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 6))
 
    for i, ax in enumerate(axes.flat):

        if i < len(images):

#             credentials, project = google.auth.default()

#             # Create a storage client using the authenticated credentials

#             storage_client = storage.Client(project=PROJECT_ID)

#             # Get a reference to the bucket

#             bucket = storage_client.bucket("advt_images")

            # Display the image in the current axis.

            ax.imshow(images[i]._pil_image)
 
            # Adjust the axis aspect ratio to maintain image proportions.

            ax.set_aspect("equal")
 
            # Disable axis ticks for a cleaner appearance.

            ax.set_xticks([])

            ax.set_yticks([])

            image = images[i]._pil_image.convert('RGB')

            draw = ImageDraw.Draw(image)

            myFont = ImageFont.load_default(size = 100)

            #myFont = ImageFont.truetype('', 255)

            draw.text((100, 780), basic_text, font = myFont, fill =(255, 255, 255))

#             font = ImageFont.load_default()

#             font_size = 100

#             while True:

#                 # Wrap the text to fit the image width

#                 wrapped_text = textwrap.fill(basic_text, width=image.width // 2)

#                 text_width, text_height = draw.textsize(wrapped_text, font=font)

#                 if text_width <= image.width and text_height <= image.height:

#                     break

#                 font_size -= 1

#                 font = ImageFont.truetype("arial.ttf", font_size)

#             x = (image.width - text_width) // 2

#             y = (image.height - text_height) // 2

#             draw.text((x, y), wrapped_text, font=font, fill=text_color)

            filename = str(uuid.uuid4())

            filename1 = "images/"+filename +"_eng"+ ".png"

            image.save(filename1)

            image = images[i]._pil_image.convert('RGB')

            draw = ImageDraw.Draw(image)

            myFont = ImageFont.load_default(size = 100)

            #myFont = ImageFont.truetype('', 255)

            draw.text((100, 780), lang_resp, font = myFont, fill =(255, 255, 255))

#             font_size = 100

#             while True:

#                 # Wrap the text to fit the image width

#                 wrapped_text = textwrap.fill(lang_resp, width=image.width // 2)

#                 text_width, text_height = draw.textsize(wrapped_text, font=font)

#                 if text_width <= image.width and text_height <= image.height:

#                     break

#                 font_size -= 1

#                 font = ImageFont.truetype("arial.ttf", font_size)

#             x = (image.width - text_width) // 2

#             y = (image.height - text_height) // 2

#             draw.text((x, y), wrapped_text, font=font, fill=text_color)

#             filename = str(uuid.uuid4())

            filename2 = "images/"+filename +"_vern"+ ".png"

            image.save(filename2)


            # image.show()

            # image = images[i]._pil_image.convert('RGB')

            # draw = ImageDraw.Draw(image)

            # myFont = ImageFont.load_default(size = 100)

            # draw.text((180, 780), lang_resp, font = myFont, fill =(255, 255, 255))

            # filename = str(uuid.uuid4())

            # filename = "images/"+filename +"_vern"+ ".png"

            # image.save(filename)

            # image.show()

            # #filename = f"image_{i}.jpg"

            # image = images[i]._pil_image.convert('RGB')

            # filename = file_name+"image"+str(i)+".jpg"

            # # 4. Construct the full path to the destination file

            # target_file = os.path.join("images/", filename)  # Adjust the new filename if needed

            # # 5. Save the image to the target folder

            # image.save(target_file)        

            """

            #save to blob

            image_bb = images[i]._pil_image.convert('RGB')

            filename_bb = file_name+"image"+str(i)+".jpg"

            image_bb.save(filename_bb, format="JPEG")

            blob = bucket.blob(filename_bb)

            blob.upload_from_filename(filename_bb)

            """

        else:

            # Hide empty subplots to avoid displaying blank axes.

            ax.axis("off")
##################################################################################
#Code to generate an image using gen ai

def image_gen(festival,lob,offer,basic_text,lang_resp):

    festival = "Diwali"

    lob ="kitchen"

    prompt = """

    You are an interior designing bot with expertise in generating photo-realistic images of living spaces. 

    You need to create an image of a dining room which is decorated for celebrating the festival of Navratra. 

    The dining room has newly crafted wooden dining table and chairs in the middle and a big wooden crockery 

    cabinet with transparent glass doors in the background. The room is brightly coloured which soothes the eyes. 

    The dining table and chairs should occupy major portion of the image. 

    The dining table is laden with rasgullas and other delicacies. The image should look realistic.

    """

    response = generation_model.generate_images(

        prompt=prompt,

        number_of_images=2,

    )

    display_images_in_grid(response.images,basic_text,lang_resp)
################################################################################3


# Add navbar
st.markdown("""
<style>
.navbar {
    background-color: #003364;
    color: #ffffff;
    padding: 10px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    border-radius: 5px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.3);
}
</style>
<div class="navbar">Asian Paints</div>
""", unsafe_allow_html=True)

# Add container div
container = st.container()

# Add selectboxes and text input inside the container
with container:
    st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    festival = st.selectbox(
        'Please select festival from the drop down',
        ('Holi', 'Diwali', 'Pongal' , 'Christmas'),
        key='festival'
    )

    lob = st.selectbox(
        'Please select Line of Business from the drop down',
        ('Kitchen', 'Home Decour', 'Bath' , 'Interior Designs', 'Wallpapers', 'Paints'),
        key='lob'
    )

    offer = st.selectbox(
        'Please select offer from the drop down',
        ('10', '20', '30'),
        key='offer'
    )

    lang = st.selectbox(
        'Please select language from the drop down',
        ('Hindi', 'English', 'Bengali' , 'Urdu'),
        key='language'
    )

    target = st.selectbox(
        'Please select target audiance from the drop down',
        ('Kids' , 'family'),
        key='target'
    )

    user_prompt = st.text_input("Enter additional prompt 👇", key='Prompt')

# Add spacer
st.markdown("""
<div style="height: 20px;"></div>
""", unsafe_allow_html=True)

# Add container for button
button_container = st.container()

# Add button inside the container
with button_container:
    if st.button('Generate', key='generate_button'):
        st.title(user_prompt)
        PromptForAi = f"Generate a banner for {festival} Festival. The banner should include text specifying {offer} on {lob} in {lang}. The banner should include images related to {festival} and {lob} in a collage template."
        print(PromptForAi)
        #image_creation(PromptForAi , "temp.jpg")
st.markdown("""
<style>
.footer {
    background-color:  #003364;
    color: #ffffff;
    padding: 10px;
    text-align: center;
    font-size: 14px;
    font-weight: bold;
    border-radius: 10px;
    box-shadow: 0px -2px 5px rgba(0,0,0,0.3);
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
}
</style>
<div class="footer">© 2023 Asian Paints. All rights reserved.</div>
""", unsafe_allow_html=True)


### Run the application
if __name__ == "__main__":
    # festival = festival
    # lob = lob
    # offer = offers
    # lang = language
    
    basic_text = text_gen(festival,lob,offer)
    basic_text = basic_text.replace("\n"," ")
    lang_resp = lang_trans(festival,lob,offer,basic_text,lang)
    print(basic_text)
    print(lang_resp)
    image_gen(festival,lob,offer,basic_text,lang_resp)
