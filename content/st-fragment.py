import streamlit as st

st.subheader("st.fragment")

st.warning("👟 Announcing the general availability of st.fragment, a decorator that lets you rerun functions independently of the whole page.")
st.page_link("https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment", label="Read Docs", icon=":material/menu_book:")

st.subheader("Example")
st.write("""
  This example demonstrates how elements both inside and outside of a fragement update with each app or fragment rerun. 
  In this app, clicking "Rerun full app" will increment both counters and update all values displayed in the app. 
  In contrast, clicking "Rerun fragment" will only increment the counter within the fragment. 
  In this case, the `st.write` command inside the fragment will update the app's frontend, 
  but the two `st.write` commands outside the fragment will not update the frontend.
""")
with st.echo():
  if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

  @st.fragment
  def my_fragment():
      st.session_state.fragment_runs += 1
      st.button("Rerun fragment")
      st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")
  
  st.session_state.app_runs += 1
  my_fragment()
  st.button("Rerun full app")
  st.write(f"Full app says it ran {st.session_state.app_runs} times.")
  st.write(f"Full app sees that fragment ran {st.session_state.fragment_runs} times.")
