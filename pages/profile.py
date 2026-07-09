import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]
my=mydb["user_info"]
@st.dialog("CHANGE PASSWORD")
def cp():
    t1=st.text_input("Enter the old password")
    t2=st.text_input("Enter the new password")
    if st.button("Change Password"):
        my.execute("update user_info set password="+"'"+t2+"'"+" where password="+"'"+t1+"'"+"")
        st.success("Password Changed successfully")
        conn.commit()
    if st.button("Go to Main Menu"):
        st.switch_page("main.py")

#login check
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.error("First Login !!!")
       st.stop()
conn=mysql.connector.connect(host="127.0.0.1",user="root",database="login",passwd="")
my=conn.cursor()
st.header("This is the Profile page")
st.success(f"Welcome :{st.session_state['username']}")


c1,c2,c3=st.columns(3)
if c1.button("Logout",use_container_width=True):
       del st.session_state["username"]
       st.switch_page("main.py")
if c2.button("See Profile",use_container_width=True):
       str1=st.session_state["uname"]
       str2=st.session_state["password"]
       res=my.find({"uname":str1,"password":str2})
       for i in res:
           st.success(i["password"])
           st.success(i["mobile"])
           st.success(i["email"])
           st.success(i["dob"])

if c3.button("Change Password",use_container_width=True):
       cp()
       

