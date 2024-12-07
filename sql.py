from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Loading Gemini
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])

    return response.text


#Retriving Data

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()

    return rows


#Defining prompt

prompt=["""
You are an expert in converting English questions to sql code! The SQL dataabse has the name STUDENT and has the following columns - NAME,CLASS , SECTION \n For example,\nExample 1 - How many entries of records are present? the sql command will be something like this SELECT COUNT(*) FROM STUDENT ; also the sql code should not have ''' in beginning or in the end and sql word in output 

"""]



st.set_page_config(page_title="I can Retrive any query")
st.header("Gemini app to Retrieve SQL Data")

question = st.text_input("Input:",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The response is :")
    for row in response:
        print(row)
        st.header(row)

