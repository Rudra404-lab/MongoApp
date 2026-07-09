import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Check whether a number is palindrome or not :")
t1=st.slider("Select a number",1,500)
if st.button("OK"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    st.success(f"Reverse={s}")
    if s==t1:
        st.success("PALINDROME")
    else:
        st.success("NOT A PALINDROME")

st.code('''import streamlit as st
st.title("Check whether a number is palindrome or not :")
t1=st.slider("Select a number",1,500)
if st.button("OK"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    st.success(f"Reverse={s}")
    if s==t1:
        st.success("PALINDROME")
    else:
        st.success("NOT A PALINDROME")''')
