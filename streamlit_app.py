import streamlit as st

st.set_page_config(page_title="Streamlit Releases", page_icon="🗺️")

st.title('🗺️ Streamlit Releases')

pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About", icon=":material/local_library:")
    ],
    "Version 1.37.0" : [
        st.Page("content/st-context.py", title="st.context", icon=":material/nutrition:"),
        st.Page("content/st-feedback.py", title="st.feedback", icon=":material/handyman:"),
        st.Page("content/st-fragment.py", title="st.fragment", icon=":material/handyman:"),
    ],
}

pg = st.navigation(pages)
pg.run()
