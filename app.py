import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and DataFrame
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Mobile Price Predictor")

# Brand
brand = st.selectbox('Brand', df['Brand'].unique())

# Model
model = st.selectbox('Model', df['Model'].unique())

# RAM
ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Storage
storage = st.selectbox('Storage (GB)', [32, 64, 128, 256])

# Battery Capacity
battery_capacity = st.selectbox('Battery Capacity (mAh)', [1821,2227,2815,4025,2942,3095,3300,3110,4115,4000,4250,4310,4500,4614,5020,5000,5160,6000])

# Create DataFrame for the query
query_df = pd.DataFrame([[brand, model, ram, storage, battery_capacity]],
                        columns=['Brand', 'Model', 'RAM ', 'Storage ', 'Battery Capacity (mAh)'])

# Predict using the model
prediction = pipe.predict(query_df)

# Display prediction
st.title("The predicted price is " + str(int(np.exp(prediction[0]))))
