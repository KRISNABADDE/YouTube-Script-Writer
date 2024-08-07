import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import HfFolder
import os
from utils import generate_script

# Load environment variables
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')

if not HUGGINGFACEHUB_API_TOKEN:
    st.error("Hugging Face API token is missing. Please check your .env file.")
    st.stop()  # Stop further execution if the token is not found

# Set the token explicitly
HfFolder.save_token(HUGGINGFACEHUB_API_TOKEN)

# Applying Styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
    }
</style>""", unsafe_allow_html=True)

st.title('❤️ YouTube Script Writing Tool') 

# Captures User Inputs
prompt = st.text_input('Please provide the topic of the video', key="prompt")  # The box for the text prompt
video_length = st.text_input('Expected Video Length 🕒 (in minutes)', key="video_length")  # The box for the text prompt
creativity = st.slider('Creativity limit ✨ - (0 LOW || 1 HIGH)', 0.0, 1.0, 0.5, step=0.1)

submit = st.button("Generate Script for me")

if submit:
    search_result, title, script = generate_script(prompt, video_length, creativity)
    # Let's generate the script
    st.success('Hope you like this script ❤️')

    # Display Title
    st.subheader("Title:🔥")
    st.write(title)

    # Display Video Script
    st.subheader("Your Video Script:📝")
    st.write(script)

    # Display Search Engine Result
    st.subheader("Check Out - DuckDuckGo Search:🔍")
    with st.expander('Show me 👀'): 
        st.info(search_result)