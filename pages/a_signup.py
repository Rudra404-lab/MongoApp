import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://rudra1951:<db_password>@cluster0.e1nvcku.mongodb.net/?appName=Cluster0")
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
       my.insert_one({"uname":t1,"password":t2,"mobile":str(t3),"email":str(t4),"dob":str(t5)})
       st.success("✅ Sign Up Successfully")
