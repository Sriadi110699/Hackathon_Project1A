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
import glob, os
from pathlib import Path as p
###################################################################################
def text_gen(festival,lob,offer):

    if lob =="Kitchen":
        lob = "kitchen makeovers"
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

            myFont = ImageFont.truetype('ttf_files/hindi.ttf',size = 100)

            #myFont = ImageFont.truetype('', 255)

            draw.text((100, 780), lang_resp, font = myFont, fill =(255, 255, 255))


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

    # festival = "Diwali"

    # lob ="kitchen"

    # prompt = "

    # You are an interior designing bot with expertise in generating photo-realistic images of living spaces. 

    # You need to create an image of a dining room which is decorated for celebrating the festival of Navratra. 

    # The dining room has newly crafted wooden dining table and chairs in the middle and a big wooden crockery 

    # cabinet with transparent glass doors in the background. The room is brightly coloured which soothes the eyes. 

    # The dining table and chairs should occupy major portion of the image. 

    # The dining table is laden with rasgullas and other delicacies. The image should look realistic.

    # "

    if (festival == 'Diwali') & (lob == 'Kitchen'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a kitchen with newly fitted cabinets, chimney and a stovetop on the night of Diwali. The kitchen's island is laden with sweets and snacks. Firecrackers can be seen bursting outside through the window on the left. The image should look realistic."
    elif(festival == 'Diwali')& (lob == 'Home Decour'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bedroom with newly furbished beds, curtains, lamps, side tables and wardrobes. The wooden ply of beds, side tables and wardrobes should be of the same wood type, and it should complement the paint on the walls. The room is lit with string lights, and firecrackers can be seen bursting through the window on the left. The image should look realistic."
    elif(festival == 'Diwali')& (lob == 'Bath'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a luxurious bathroom. The bathroom has new plumbing and fitted with a number of stylish taps and showerheads. Water is drizzling down the showerhead. The bathroom floor has been laid with new and stylish tiles and the walls are tiled with realistic-looking tiles. There is a glass wall separating the bath space from the wash basin. The wash basin looks stylish with amazingly-looking faucet. The image should look realistic."
    elif(festival == 'Diwali')& (lob == 'Interior Designs'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bedroom with newly furbished beds, curtains, lamps, side tables and wardrobes. The wooden ply of beds, side tables and wardrobes should be of the same wood type, and it should complement the paint on the walls. The room is lit with string lights, and firecrackers can be seen bursting through the window on the left. The image should look realistic."
    elif(festival == 'Diwali')& (lob == 'Wallpapers'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bedroom with new wallpapers. The wallpapers should be in variety, which can include solid colours, stripes, floral patterns, abstract patterns. The scene is warm and welcoming. The image should look realistic."
    elif(festival == 'Diwali')& (lob == 'Paints'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bungalow on Diwali night. The bungalow has been newly painted with bright colors. The bungalow is decorated with string lights, while its porch is decorated with rangoli and diyas. Firecrackers can be seen bursting in the night sky. The bungalow should cover major potion of the image. There is a small lawn in the front of the bungalow, and a retro car is parked in front of the bungalow. The image should look realistic."


    
    elif (festival == 'Holi') & (lob == 'Kitchen'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a kitchen which is decorated for celebrating the festival of Holi. The kitchen has newly fitted cabinets. Sweets are kept on the kitchen's island, as well as some Holi colours are piled on dishes on the kitchen island. The view is positive. The image should look realistic."
    elif(festival == 'Holi')& (lob == 'Home Decour'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Holi. The living room has newly furbished sofas and coffee table in the foreground. The sofas and coffee table should occupy major portion of the image. Sweets are kept on the coffee table, as well as some Holi colours are piled on dishes on the coffee table. The view is positive. The image should look realistic."
    elif(festival == 'Holi')& (lob == 'Bath'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a luxurious bathroom. The bathroom has new plumbing and fitted with a number of stylish taps and showerheads. Water is drizzling down the showerhead. The bathroom floor has been laid with new and stylish tiles and the walls are tiled with realistic-looking tiles. There is a glass wall separating the bath space from the wash basin. The wash basin looks stylish with amazingly-looking faucet. The image should look realistic."
    elif(festival == 'Holi')& (lob == 'Interior Designs'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Holi. The living room has newly furbished sofas and coffee table in the foreground. The sofas and coffee table should occupy major portion of the image. Sweets are kept on the coffee table, as well as some Holi colours are piled on dishes on the coffee table. The view is positive. The image should look realistic."
    elif(festival == 'Holi')& (lob == 'Wallpapers'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Holi. The living room is renovated by applying new colorful wallpapers. The walls should be more visible in the image. Sweets are kept on the coffee table, as well as some Holi colours are piled on dishes on the coffee table. The Holi colours should not be scattered on furniture and floors. The view is positive. The image should look realistic."
    elif(festival == 'Holi')& (lob == 'Paints'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bungalow on the day of Holi. The bungalow has been newly painted with bright paints and not with Holi colors. There are some people playing with colors in the lawn in front of the bungalow. The bungalow should cover major portion of the image. The image should look realistic."


    
    elif (festival == 'Navratra') & (lob == 'Kitchen'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a kitchen with newly fitted cabinets, chimney and a stovetop on the night of Navratra. The kitchen's island is laden with sweets and snacks. Pair of dandiyas is also kept on the kitchen island. The image should look realistic, and the image should be closed up."
    elif(festival == 'Navratra')& (lob == 'Home Decour'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a dining room which is decorated for celebrating the festival of Navratra. The dining room has newly crafted wooden dining table and chairs in the middle and a big wooden crockery cabinet with transparent glass doors in the background. The room is brightly coloured which soothes the eyes. The dining table and chairs should occupy major portion of the image. The dining table is laden with rasgullas and other delicacies. The image should look realistic."
    elif(festival == 'Navratra')& (lob == 'Bath'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a luxurious bathroom. The bathroom has new plumbing and fitted with a number of stylish taps and showerheads. Water is drizzling down the showerhead. The bathroom floor has been laid with new and stylish tiles and the walls are tiled with realistic-looking tiles. There is a glass wall separating the bath space from the wash basin. The wash basin looks stylish with amazingly-looking faucet. The image should look realistic."
    elif(festival == 'Navratra')& (lob == 'Interior Designs'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a dining room which is decorated for celebrating the festival of Navratra. The dining room has newly crafted wooden dining table and chairs in the middle and a big wooden crockery cabinet with transparent glass doors in the background. The room is brightly coloured which soothes the eyes. The dining table and chairs should occupy major portion of the image. The dining table is laden with rasgullas and other delicacies. The image should look realistic."
    elif(festival == 'Navratra')& (lob == 'Wallpapers'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a dining room which is decorated for celebrating the festival of Navratra. The dining room is newly renovated by applying new wallpapers with very low density of floral patterns that are pleasing and soothing to the eyes. There is a wooden dining table and chairs in the middle. The room is brightly coloured which soothes the eyes. The walls should occupy major portion of the image. The dining table is laden with rasgullas and other delicacies. The image should look realistic."
    elif(festival == 'Navratra')& (lob == 'Paints'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bungalow on the night of Navratra. The bungalow has been newly painted with bright paints. There are some people playing Garba and Dandiya and are wearing traditional clothes in the lawn in front of the bungalow. The bungalow is decorated with string lights and torans. The bungalow should cover major portion of the image. The image should look realistic."




    elif (festival == 'Christmas') & (lob == 'Kitchen'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a kitchen with newly fitted cabinets, chimney and a stovetop on the night of Christmas. The kitchen's island is laden with christmas cake, cookies, candy canes and other sweets. Snowfall can be seen outside through the window on the left. The scene looks warm and pleasing. The image should look realistic."
    elif(festival == 'Christmas')& (lob == 'Home Decour'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Christmas. The living room has newly furbished sofas and coffee table in the foreground. The sofas and coffee table should occupy major portion of the image. The Christmas tree has been fully decorated with lights and other ornaments and is kept in the background. Snow can be seen from the window on the left side. The family is very happy. The image should look realistic."
    elif(festival == 'Christmas')& (lob == 'Bath'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a luxurious bathroom. The bathroom has new plumbing and fitted with a number of stylish taps and showerheads. Water is drizzling down the showerhead. The bathroom floor has been laid with new and stylish tiles and the walls are tiled with realistic-looking tiles. There is a glass wall separating the bath space from the wash basin. The wash basin looks stylish with amazingly-looking faucet. The image should look realistic."
    elif(festival == 'Christmas')& (lob == 'Interior Designs'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Christmas. The living room has newly furbished sofas and coffee table in the foreground. The sofas and coffee table should occupy major portion of the image. The Christmas tree has been fully decorated with lights and other ornaments and is kept in the background. Snow can be seen from the window on the left side. The family is very happy. The image should look realistic."
    elif(festival == 'Christmas')& (lob == 'Wallpapers'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a living room which is decorated for celebrating the festival of Christmas. The living room has been renovated by applying new wallpapers that complement the christmas decoration. The Christmas tree has been fully decorated with lights and other ornaments and is kept in the background. The wallpaper on the walls should appear more on the image. The scene looks warm and pleasing. The image should look realistic. "
    elif(festival == 'Christmas')& (lob == 'Paints'):
        prompt = "You are an interior designing bot with expertise in generating photo-realistic images of living spaces. You need to create an image of a bungalow on Christmas night. The bungalow has been newly painted with bright colors. The bungalow is decorated with string lights, while its porch is decorated with Santa Claus and reindeer blowups. The Christmas tree is also kept in the porch and is fully decorated. The bungalow should cover major potion of the image. There is a small lawn in the front of the bungalow. The image should look realistic."







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
        ('Holi', 'Diwali', 'Navratra' , 'Christmas'),
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

    #delete 
    image_folder = p.cwd() / "images"
    p(image_folder).mkdir(parents=True, exist_ok=True)
    
    basic_text = text_gen(festival,lob,offer)
    basic_text = basic_text.replace("\n"," ")
    lang_resp = lang_trans(festival,lob,offer,basic_text,lang)
    print(basic_text)
    print(lang_resp)
    image_gen(festival,lob,offer,basic_text,lang_resp)
    st.header("Below is the A.I. generated Banners :"+"\n", divider='rainbow')
    list_of_img = glob.glob("images/*")
    st.image(list_of_img, use_column_width=True)
