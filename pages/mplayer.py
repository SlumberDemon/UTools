import streamlit as st
from streamlit_elements import media, mui, dashboard, elements

with elements("mplayer"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="MPlayer", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url, width="100%", height="100%", controls=True)