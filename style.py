import streamlit as st
def add_bg_from_url():
    new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">hello</p>'
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/originals/95/ea/f8/95eaf8f43b75d58122081002ebf31d61.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()