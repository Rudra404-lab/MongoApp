import streamlit as st
import pymongo
from urllib.parse import quote_plus

username = quote_plus('<username>')
password = quote_plus('<password>')
cluster = '<clusterName>'
authSource = '<authSource>'
authMechanism = '<authMechanism>'

uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism

client = pymongo.MongoClient(uri)

result = client["<dbName"]["<collName>"].find()
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
