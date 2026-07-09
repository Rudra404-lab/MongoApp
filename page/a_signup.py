import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["ojt"]
my=mydb["user_info"]

st.title("S i g n U p")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
t3=st.text_input("Mobile Number")
t4=st.text_input("Email Id")
t5=st.date_input("DOB")


b1=st.button("SIGN UP")

if b1:
       my.insert_one({"uname":t1,"password":t2,"mobile":str(t3),"email":t4,"dob":str(t5)})
       st.success("✅ Sign Up Successfully")
