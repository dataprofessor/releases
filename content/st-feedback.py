import streamlit as st

st.subheader("st.feedback")

st.warning("⭐ Introducing st.feedback to collect ratings and sentiment from your users!")

st.subheader("Display stars")
st.write("Display a feedback widget with stars, and show the selected sentiment:")
with st.echo():
  sentiment_mapping = ["one", "two", "three", "four", "five"]
  selected = st.feedback("stars")
  if selected is not None:
      st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

st.divider()

st.subheader("Display thumbs up/down")
st.write("Display a feedback widget with stars, and show the selected sentiment:")
with st.echo():
  sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
  selected = st.feedback("thumbs")
  if selected is not None:
      st.markdown(f"You selected: {sentiment_mapping[selected]}")

st.page_link("https://docs.streamlit.io/", label="Docs", icon="🌎")
