import streamlit as st

st.subheader("st.context")

st.write("🍪 Introducing `st.context` to read headers and cookies!")

st.write("**context.headers**")
with st.echo():
  st.context.headers

st.divider()

st.write("**context.cookies**")
with st.echo():
  st.context.cookies
