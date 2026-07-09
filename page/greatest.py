import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()

st.title("Greatest among three numbers")
t1=st.number_input("1st number")
t2=st.number_input("2nd number")
t3=st.number_input("3rd number")
if st.button("Find"):
    if (t1>t2 and t1>t3):
        st.success(f"Greatest={t1}")
    elif (t2>t1 and t2>t3):
        st.success(f"Greatest={t2}")
    else:
        st.success(f"Greatest={t3}")

st.code('''import streamlit as st
st.title("Greatest among three numbers")
t1=st.number_input("1st number")
t2=st.number_input("2nd number")
t3=st.number_input("3rd number")
if st.button("Find"):
    if (t1>t2 and t1>t3):
        st.success(f"Greatest={t1}")
    elif (t2>t1 and t2>t3):
        st.success(f"Greatest={t2}")
    else:
        st.success(f"Greatest={t3}")''')
