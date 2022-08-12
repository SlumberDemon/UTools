import time
import validators
import streamlit as st
from pytube import YouTube


st.markdown(
    """
# Udownload
Download videos
"""
)
st.sidebar.markdown(
    """# Udownload
Download videos"""
)


video = True

URL = st.text_input(
    label="Url",
    placeholder="Enter video url here",
    help="Make sure you entered the link correctly",
    key="url",
)

if URL:
    if validators.url(URL) is True:
        video = False
    else:
        st.warning(
            "Make sure the url is in this format: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )

type = st.radio("Type", ("mp3", "mp4"), disabled=video)

if type and URL:
    yt = YouTube(URL)
    try:
        if yt.title:
            if video == False:
                if type == "mp3":
                    st.write("#### Select audio quality to download")
                    with st.spinner("Fetching..."):
                        for stream in yt.streams.filter(
                            only_audio=True,
                            progressive=False,
                            type="audio",
                            abr="128kbps",
                            only_video=False,
                        ):
                            video = yt.streams.get_by_itag(stream.itag)
                            v = video.download(output_path="/app/slumberapps/cache")
                            with open(v, "rb") as f:
                                _bytes = f.read()
                            st.download_button(
                                label=f"{stream.abr}",
                                data=_bytes,
                                file_name=f"{yt.title.replace(' ', '_')}.mp3",
                                key=stream.itag,
                            )
                            with st.spinner("Searching..."):
                                time.sleep(4)
                elif type == "mp4":
                    st.write("#### Select video quality to download")
                    with st.spinner("Fetching..."):
                        for stream in yt.streams.filter(
                            file_extension="mp4",
                            type="video",
                            only_audio=False,
                            only_video=False,
                            progressive=True,
                        ):
                            video = yt.streams.get_by_itag(stream.itag)
                            v = video.download(output_path="/app/slumberapps/cache")
                            with open(v, "rb") as f:
                                _bytes = f.read()
                            st.download_button(
                                label=f"{stream.resolution}",
                                data=_bytes,
                                file_name=f"{yt.title.replace(' ', '_')}.mp4",
                                key=stream.itag,
                            )
                            with st.spinner("Searching..."):
                                time.sleep(4)
        else:
            st.warning("Video not found")
    except:
        st.warning(
            "Unable to fetch video, You might be getting [ratelimited](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)"
        )