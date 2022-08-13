import streamlit as st
from streamlit_elements import media

media_url = st.text_input("Media url", placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
media.Player(url=media_url, width="100%", height="100%", controls=True)