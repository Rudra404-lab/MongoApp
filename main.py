import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://rudra1951:<db_password>@cluster0.e1nvcku.mongodb.net/?appName=Cluster0")
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
mydb=conn["ojt"]
my=mydb["user_info"]

st.title("🐍All the basic python code")
st.snow()


st.header("Welcome! Please Login First")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("🔑 SIGNIN")
valid=0
if b1:
       ans=my.find({"uname":t1,"password":t2})
       for i in ans:
              valid=valid+1
              st.session_state["username"]=i['uname']
              st.session_state["password"]=i['password']
              st.switch_page("pages/profile.py")
                             
       if valid==0:
              st.success("Invalid User Login Details")


st.image("image1.jpg")

st.logo("logo1.png")


sidebar_css = """
<style>
[data-testid="stSidebar"] {
    background-color: #0068c9; /* Uses transparency */
}
</style>
"""
st.markdown(sidebar_css, unsafe_allow_html=True)
b2=st.button("SIGNUP")

