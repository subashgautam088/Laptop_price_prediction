import streamlit as st 
import pickle
import numpy as np

# Import the model
pipe = pickle.load(open('forest_model.pkl', 'rb'))
df = pickle.load(open('df2.pkl', 'rb'))

# Title
st.title("Laptop Price Prediction")

# Brand
company = st.selectbox('Brand', sorted(df['Company'].unique()))

# Type of laptop
type = st.selectbox("Type", sorted(df['TypeName'].unique()))

# Ram
ram = st.selectbox("RAM", sorted(df['Ram(GB)'].unique()))

# Weight
weight = st.number_input("Weight of the Laptop")

# TouchScreen
touchscreen = st.selectbox("TouchScreen", ['No', 'Yes'])

# Ips
ips = st.selectbox("IPS", ['No', 'Yes'])

# Screen Size
screen_size = st.slider("Screen size in Inches", 10.0, 18.0, 13.0)

# Resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# Cpu
cpu = st.selectbox("CPU", sorted(df['Cpu brand'].unique()))

# HDD
hdd = st.selectbox("HDD(in GB)", [0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox("SSD(in GB)", [0,128,256,512,1024,2048])

#Hybrid
hybrid = st.selectbox("Hybrid", ['No','Yes'])

# Gpu
gpu = st.selectbox('GPU', sorted(df['Gpu brand'].unique()))

# os 
os = st.selectbox("OS", df['os'].unique())

if st.button('Predict Price'):
    # Query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
        
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2) + (y_res**2))**0.5/screen_size
    query = np.array([company, type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    
    query = query.reshape(1,12)
    st.title("The predicted price of this laptop is ₹" + str(int(np.exp(pipe.predict(query)[0]))))
    
    