from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision Api and get response
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to pre-process the image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

input_prompts = """
You are an expert pharmaceutical chemist where you need to see the tablets from the image
and also provide the details of every drug/tablet item with the below format:

1. Examine the image carefully and identify the tablets depicted.
2. Describe the uses and functionalities of each tablet shown in the image.
3. Provide information on the intended purposes, features, and typical applications of the tablets.
4. If possible, include any notable specifications or distinguishing characteristics of each tablet.
5. Ensure clarity and conciseness in your descriptions, focusing on key details.
"""

# Initialize our Streamlit app
st.set_page_config(page_title="AI Chemist App")

st.header("AI Chemist App")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me")

if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompts)
        st.subheader("The response is:")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
