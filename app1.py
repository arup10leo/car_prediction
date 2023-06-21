import streamlit as st
import pickle
import numpy as np
from sklearn import *

pipe = pickle.load(open('pipe2.pkl', 'rb'))

df = pickle.load(open('data2.pkl', 'rb'))

st.title("Car predictor")

# symboling
symboling = st.selectbox('Symboling', df['symboling'].unique())

# aspiration
aspiration = st.selectbox('aspiration', df['aspiration'].unique())

# doornumber
doors = st.selectbox('How many doors want?', df['doornumber'].unique())


# carbody
carbody = st.selectbox(
    'Which type of carbody you are looking for?', df['carbody'].unique())


# drivewheel
drivewheel = st.selectbox(
    'Which type of drivewheel needed?', df['drivewheel'].unique())

# wheelbase
wheelbase = st.number_input('wheelbase')

# curbweight
curbweight = st.selectbox('curbweight', df['curbweight'].unique())

# enginetype
enginetype = st.selectbox('enginetype', df['enginetype'].unique())

# cylinder
cylinder = st.selectbox('Number of cylinders', df['cylindernumber'].unique())

# enginesize
enginesize = st.slider('Engine Size', 65.0, 326.0)

# fuel
fuel = st.selectbox('fuelsystem', df['fuelsystem'].unique())


# boreratio
boreratio = st.selectbox('boreratio', df['boreratio'].unique())

# stroke
stroke = st.selectbox('stroke', df['stroke'].unique())

# compressionratio
compressionratio = st.selectbox(
    'compressionratio', df['compressionratio'].unique())

# horsepower
horsepower = st.number_input('What will be the horsepower?')


# rpm
rpm = st.selectbox('RPM', [5000, 5500, 5800, 4250,
                   5400, 5100, 4800, 6000, 4750, 4650, 4200])

# citympg
citympg = st.number_input('What will be the citympg?')

# highwaympg
highwaympg = st.number_input('What will be the highwaympg?')


# volume
vol = st.slider('Car Volume', 452700.0, 846000.0)

# brand
brand = st.selectbox('Prefered Brand', df['CarBrand'].unique())


if st.button('Predict Price'):

    query = np.array([symboling, aspiration, doors, carbody, drivewheel, wheelbase, curbweight, enginetype,
                     cylinder, enginesize, fuel, boreratio, stroke, compressionratio, horsepower, rpm, citympg, highwaympg, vol, brand])

    query = query.reshape(1, 20)
    st.title("Rs."+str(int(np.exp(pipe.predict(query)))))
