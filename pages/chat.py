import streamlit as st
import openai

openai.api_key = ""

st.markdown("# Article name finder")
st.sidebar.markdown("# Chat")

with st.form("articleupload"):
    input = st.text_input(label="Input")
    transcribe = st.form_submit_button(label="Start")

if transcribe:
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "system", "content": 'youre an unhelpful assitant who enjoys mcdonalds and giving false information'},
                        {"role": "user", "content": f'Create a list of all the people named in this document and who they are:  {input}'}
              ])
    st.write(response.choices[0].message.content)