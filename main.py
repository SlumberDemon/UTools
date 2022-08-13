import streamlit as st


st.markdown("# UTools")
st.sidebar.markdown("# UTools")

st.write("Use the side menu to select a tool to use!")
with st.expander("About the tools"):
    st.write("""⬩ Udownload | Download videos \n""")
    st.write("""⬩ MPlayer | Watch videos""")
    st.write("""⬩ SleepyTube | Watch videos without restricitons""")

st.caption("[Source](https://github.com/SlumberDemon/UTools)")