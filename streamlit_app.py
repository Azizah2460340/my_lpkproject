import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("🎈 My new app")

st.markdown("*Streamlit* is **really** ***cool***.")
 
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
import streamlit as st
st.image(https://sl.bing.net/d7FSTs0JDfU, caption="Sunrise by the mountains")
