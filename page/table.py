import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Generate table of a number")
t1=st.slider("Select a number")
if st.button("Table"):
    for i in range(1,11,1):
        st.write(i*t1)

st.code('''import streamlit as st
st.title("Generate table of a number")
t1=st.slider("Select a number")
if st.button("Table"):
    for i in range(1,11,1):
        st.write(i*t1)''')
