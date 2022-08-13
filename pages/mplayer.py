import streamlit as st
from streamlit_elements import media

media_url = st.text_input("Media url", value="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
    mui.CardHeader(title="MPlayer", className="draggable")
    with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

        # This element is powered by ReactPlayer, it supports many more players other
        # than YouTube. You can check it out there: https://github.com/cookpete/react-player#props
            
        media.Player(url=media_url, width="100%", height="100%", controls=True)