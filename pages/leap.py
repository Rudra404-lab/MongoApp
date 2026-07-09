import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Check whether its a leap year or not")
x=st.slider("Select the year",1900,3000)
if st.button("Check"):
    if(x%4==0):
        st.success("Leap year")
    else:
        st.success("Not a Leap year")

st.code('''import streamlit as st
st.title("Check whether its a leap year or not")
x=st.slider("Select the year",1900,3000)
if st.button("Check"):
    if(x%4==0):
        st.success("Leap year")
    else:
        st.success("Not a Leap year")
''')
