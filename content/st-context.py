import streamlit as st

st.subheader("st.context")

st.warning("🍪 Introducing `st.context` to read headers and cookies!")
st.page_link("https://docs.streamlit.io/develop/api-reference/utilities/st.context", label="Read Docs", icon=":material/menu_book:")

st.subheader("context.headers")
st.write("Show a dictionary of headers:")
with st.echo():
  st.context.headers

st.divider()

st.subheader("context.cookies")
st.write("Show a dictionary of cookies:")
with st.echo():
  st.context.cookies
