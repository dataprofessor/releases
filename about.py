import streamlit as st

st.subheader("About")

st.info("""
  This is an interactive app for exploring recently released Streamlit features. 
  For more information, check out the following links:
        """)

st.page_link("https://docs.streamlit.io/develop/quick-reference/release-notes", label="Release notes", icon=":material/checklist:")
