import streamlit as st
from utils import PrepProcesor, columns 

import numpy as np
import pandas as pd
import joblib
html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> If you were on the Titanic, would you survive? </h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
model = joblib.load('xgbpipe.joblib')
st.title('please give us your info so we can predict this question :ship:')
passengerid = st.text_input("Input Passenger ID", '8585') 
pclass = st.selectbox("Choose class", [1,2,3])
name  = st.text_input("Input Passenger Name", 'Soheil Tehranipour')
sex = st.select_slider("Choose sex", ['male','female'])
age = st.slider("Choose age",0,100)
sibsp = st.slider("Choose siblings",0,10)
parch = st.slider("Choose parch",0,10)
ticket = st.text_input("Input Ticket Number", "8585") 
fare = st.number_input("Input Fare Price", 0,1000)
cabin = st.text_input("Input Cabin", "C52") 
embarked = st.select_slider("Did they Embark?", ['S','C','Q'])
def predict(): 
    row = np.array([passengerid,pclass,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('you survived :thumbsup:')
    else: 
        st.error('oh i am sorry you die:(  :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)

