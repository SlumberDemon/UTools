import os

import requests
import streamlit as st

TOKEN = os.getenv("TOKEN")

st.markdown(
    """
# Sleepify
Find Music
"""
)
st.sidebar.markdown(
    """# Sleepify
"""
)

QUERY = st.text_input(
    label="Search",
    placeholder="Start typing here",
    key="query",
)


AMOUNT = st.slider(
    label="Query Amount", min_value=2, max_value=25, value=5, step=1, key="amount"
)


TYPE = st.radio("Type", ["track", "artist"])

if QUERY:
    if TYPE == "track":
        with st.spinner("Searching..."):
            url = f"https://api.spotify.com/v1/search?q={QUERY}&type={TYPE}&limit={AMOUNT}"

            headers = {
                "Accept": "application/json",
                "Authorization": "Bearer " + TOKEN,
            }

            response = requests.get(url, headers=headers)
            for i in response.json()["tracks"]["items"]:
                with st.container():
                    a1, a2 = st.columns(2)
                    with a1:
                        st.image(i["album"]["images"][1]["url"])
                    with a2:
                        st.markdown(
                            f"# [`{i['album']['name']}`]({i['album']['external_urls']['spotify']})"
                        )
                        for a in i["artists"]:
                            st.write(a["name"])
    elif TYPE == "artist":
        with st.spinner("Searching..."):
            url = f"https://api.spotify.com/v1/search?q={QUERY}&type={TYPE}&limit={AMOUNT}"

            headers = {
                "Accept": "application/json",
                "Authorization": "Bearer BQD3yDpWhQv-gWrssanLct4Pkaa1nk7T96OQFPuGHBDHROB1KX8CHm_p7bMV9Ir0dLfSSkX-2AK5C81rut7lHirW2lFQSuDunvxN9lamXsUZcIzXZyE",
            }

            response = requests.get(url, headers=headers)

            for i in response.json()["artists"]["items"]:
                with st.container():
                    a1, a2 = st.columns(2)
                    with a1:
                        st.image(i["images"][0]["url"])
                    with a2:
                        st.markdown(
                            f"# [`{i['name']}`]({i['external_urls']['spotify']})"
                        )
                        st.write(f"Followers: {i['followers']['total']}")
                        st.write(f"Popularity: {i['popularity']}")
