import streamlit as st
import numpy as np
import os


with st.container():
    st.header('Registration Form')
    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.selectbox('',
                          ('Mr','Mrs','Miss'))
    with col2:
        name=st.text_input('First name')
    with col3:
        lastname=st.text_input('Last name')

    designation = st.selectbox('Desgination',
                          ('Software','Technical Lead','Manager'))
    date_of_birth=st.date_input('Date of Birth')
    radio_gender=st.radio("Select Gender", ('Male', 'Female', 'Preferred Not to Say'))  
    age=st.slider('Age',1,150,1)       
    submit_button=st.button('Submit Button')

    if submit_button:
        info={
            "Name": title+ ' '+name+' '+lastname,
            'Date of Birth': date_of_birth,
            'Designation':designation,
            'Gender':radio_gender,
            'Age':age
        }
        st.write(info)       

