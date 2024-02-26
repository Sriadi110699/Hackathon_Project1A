import streamlit as st

festival = st.selectbox(
    'Please select festival from the drop down',
    ('Holi', 'Diwali', 'Pongal' , 'Christmas' , 'Republic Day' , 'Independence  Day'))

lob = st.selectbox(
    'Please select Line of Business from the drop down',
    ('Kitchen', 'Home Decour', 'Bath' , 'Interior Designs', 'Wallpapers'))

offers = st.selectbox(
    'Please select offer from the drop down',
    ('10', '20', '30'))

language = st.selectbox(
    'Please select language from the drop down',
    ('Hindi', 'English', 'Bengali' , 'Urdu'))

target = st.selectbox(
    'Please select target audiance from the drop down',
    ('Kids' , 'family'))


Prompt = st.text_input("Enter additional prompt 👇")

if st.button('Generate'):
    st.title(Prompt)
    PromptForAi = f"Generate a banner for {festival} Festival. The banner should include text specifying {offers} on {lob} in {language}. The banner should include images related to {festival} and {lob} in a collage template."
    print(PromptForAi)
    #image_creation(PromptForAi , "temp.jpg")
    
    
