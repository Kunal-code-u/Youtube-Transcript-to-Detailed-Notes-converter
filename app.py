import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
import google.generativeai as genai
##
models = genai.list_models()
print("Available models:")
for model in models:
    print(model.name)
##

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# responsible for fetching 

prompt = """You are a YouTube video summarizer. You will be taking the transcript text and summarizing the entire video. 
Provide the important summary as a list of concise bullet points (around 250 words). 
Each point should have a **heading** followed by a brief explanation. Use the following format:

- **Heading 1:** Brief explanation.
- **Heading 2:** Brief explanation.
- **Heading 3:** Brief explanation.

Please provide the summary of the text given here: """



#  getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = ""
        for i in transcript_text:
            transcript += " " + i['text']
        return transcript
    
    except Exception as e:
        raise e
        
# getting summary based on prompt from google gemini pro     
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("models/gemini-1.5-pro-002")
    response = model.generate_content(prompt + transcript_text)
    return response.text
    
st.title("Youtube Transcript to Detailed Notes converter")
youtube_link = st.text_input("Enter the youtube video link")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg")  # default image url    

if st.button("Get detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Detailed Notes')
        st.write(summary)
    