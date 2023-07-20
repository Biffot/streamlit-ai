import os
import time

import streamlit as st
import openai
from pytube import YouTube


openai.api_key = ""

st.markdown("# Transcriber")
st.sidebar.markdown("# Transcriber")

with st.form("file_form"):
    audiofiles = st.file_uploader(label="Audio File",type=['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg'], accept_multiple_files=True)
    transcribe = st.form_submit_button(label="Start")

with st.form("youtube_form"):
    ytlink = st.text_input(label="YouTube Link", placeholder="https://youtube.com/")
    transcribeyt = st.form_submit_button(label="Start")
    
if transcribeyt:
    yt = YouTube(ytlink)
    if yt.length > 1200:
        st.write("YouTube video is too long")
    else:
        ytfiles = yt.streams.filter(only_audio = True)
        ytfile = ytfiles[0].download("/downloads")
        audio_file= open(f"{ytfile}", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        st.text_area(label=f"{yt.title}", value=transcript["text"])
        st.download_button(label="Download", data=transcript["text"], file_name=f"{yt.title}.txt")
        audio_file.close()
        while True:
            try:
                os.remove(f"{ytfile}")
                break
            except:
                time.sleep(1)
        

if transcribe:
    if audiofiles is not None:
        for audiofile in audiofiles:
            transcript = openai.Audio.transcribe("whisper-1", audiofile)
            st.text_area(label=f"{audiofile.name}", value=transcript["text"])
            st.download_button(label="Download", data=transcript["text"], file_name=f"{audiofile.name}.txt")
    else:
        st.write("No file was uploaded")