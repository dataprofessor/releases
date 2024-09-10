import streamlit as st

st.set_page_config(page_title="Streamlit Releases", page_icon="🗺️")

st.title('🗺️ Streamlit Releases')


pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About", icon=":material/local_library:")
    ],
    "Releases" : [
        st.Page("content/page1.py", title="Page 1", icon=":material/nutrition:"),
        st.Page("content/page2.py", title="Page 1", icon=":material/handyman:"),
    ]
}

pg = st.navigation(pages)
pg.run()
