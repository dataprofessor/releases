import streamlit as st

st.subheader("st.dialog")

st.warning("🍿 Announcing the general availability of st.dialog, a decorator that lets you create modal dialogs")
st.page_link("https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog", label="Read Docs", icon=":material/menu_book:")

st.subheader("Example")
st.write("""
  The following example demonstrates the basic usage of `@st.dialog`. 
  In this app, clicking "A" or "B" will open a modal dialog and prompt you to enter a reason for your vote. 
  In the modal dialog, click "Submit" to record your vote into Session State and rerun the app. 
  This will close the modal dialog since the dialog function is not called during the full-script rerun.
""")

with st.echo():
  @st.dialog("Cast your vote")
  def vote(item):
      st.write(f"Why is {item} your favorite?")
      reason = st.text_input("Because...")
      if st.button("Submit"):
          st.session_state.vote = {"item": item, "reason": reason}
          st.rerun()
  
  if "vote" not in st.session_state:
      st.write("Vote for your favorite")
      if st.button("A"):
          vote("A")
      if st.button("B"):
          vote("B")
  else:
      f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
  
