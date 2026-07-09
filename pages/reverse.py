import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Reverse a number")
t1=st.slider("Select a number",1,1000)
if st.button("REVERSE"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    st.success(f"Reverse={s}")

st.code('''import streamlit as st
st.title("Reverse a number")
t1=st.slider("Select a number",1,1000)
if st.button("REVERSE"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    st.success(f"Reverse={s}")''')
