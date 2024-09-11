import streamlit as st

st.subheader("About")

st.info("""
  This is an interactive app for exploring recently released Streamlit features. 
  For more information, check out the following links:
        """)

st.write("### Streamlit open source")
st.page_link("https://docs.streamlit.io/develop/quick-reference/release-notes", label="Release notes", icon=":material/checklist:")
st.page_link("https://docs.streamlit.io/develop/quick-reference/prerelease", label="Pre-release features", icon=":material/preview:")
st.page_link("https://roadmap.streamlit.app/", label="Streamlit roadmap", icon=":material/map:")

st.write("### Streamlit in Snowflake")
st.page_link("https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake", label="Release notes", icon=":material/checklist:")
