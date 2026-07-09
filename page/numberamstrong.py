import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Check Armstrong Number")
num = st.number_input("Enter a number")

if st.button("Check"):
    digits = str(int(num))
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    if total == int(num):
        st.success(f"{int(num)} is an Armstrong number")
    else:
        st.error(f"{int(num)} is not an Armstrong number")

st.code(''''import streamlit as st
st.title("Check Armstrong Number")
num = st.number_input("Enter a number")

if st.button("Check"):
    digits = str(int(num))
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    if total == int(num):
        st.success(f"{int(num)} is an Armstrong number")
    else:
        st.error(f"{int(num)} is not an Armstrong number")''')
