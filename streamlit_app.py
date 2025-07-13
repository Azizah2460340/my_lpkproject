import streamlit as st

st.write("S, *World!* :sunglasses:")

st.title("SELAMAT DATANG DI O-KIMIAKU")

st.markdown("*Streamlit* is **really** ***cool***.")
 
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")
