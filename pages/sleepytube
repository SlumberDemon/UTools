import time
import aiotube
import streamlit as st
from pytube import YouTube


st.markdown(
    """
# SleepyTube
Watch videos without restricitons
"""
)
st.sidebar.markdown(
    """# Alternative video watching
Watch videos without restricitons"""
)


QUERY = st.text_input(
    label="Video search",
    placeholder="Start typing here",
    key="query",
)


AMOUNT = st.slider(
    label='Video(s)',
    min_value=1,
    max_value=25,
    value=5,
    step=1,
    key="amount"
)


if QUERY:
    with st.spinner("Fetching videos..."):
        try:
            videos = aiotube.Search.videos(QUERY, int(AMOUNT))
            for video in videos.values():
                c = st.container()
                yt = YouTube(video['url'])
                for stream in yt.streams.filter(
                    file_extension="mp4",
                    type="video",
                    only_audio=False,
                    only_video=False,
                    progressive=True,
                    resolution="720p",
                ):
                    with st.spinner("Chunking video data..."):
                        try:
                            id = yt.streams.get_by_itag(stream.itag)
                            v = id.download(output_path="/app/utools/cache")
                            with open(v, "rb") as f:
                                _bytes = f.read()
                            c.video(_bytes, format="video/mp4")
                        except:
                            c.header('Video not available')
                c.markdown(f"[`{video['title']}`]({video['url']})")
                with st.spinner("Searching for more videos..."):
                    time.sleep(4)
        except:
            st.warning(
                "Unable to fetch video(s), You might be getting [ratelimited](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)"
            )