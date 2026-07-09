import streamlit as st
st.title("Add two number in python streamlit")
t1=st.text_input("Enter 1st number")
t2=st.text_input("Enter 2st number")
b1=st.button("ADD")
if b1:
    c=int(t1)+int(t2)
    st.success(f"SUM={c}")
