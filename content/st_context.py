import streamlit as st

st.subheader("st.context")

st.write("🍪 Introducing st.context to read headers and cookies!")

with st.echo():
  st.context.headers

with st.cookies():
  st.context.headers
