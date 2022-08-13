import streamlit as st
from streamlit_elements import media, mui, dashboard, elements

layout = [
    dashboard.Item("media", 0, 2, 12, 4),
]

media_url = st.text_input(
    "Media URL", value="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)

with elements("mplayer"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="MPlayer", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url, width="100%", height="100%", controls=True)