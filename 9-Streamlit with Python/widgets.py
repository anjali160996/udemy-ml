import streamlit as st
import pandas as pd

st.title('Streamlit Text input')

name = st.text_input('Enter your name:')

age=st.slider('Enter your age:', min_value=0, max_value=100, value=25)

st.write('Your age is:', age)

options = ['Male', 'Female', 'Other']
choice = st.selectbox('Choose your gender:', options)
st.write('You selected:', choice)


if name: 
    st.write('Hello,', name)


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 28, 35, 32],
    "Gender": ["Male", "Female", "Male", "Male", "Female"]
}

df = pd.DataFrame(data)
df.to_csv('sampeleData.csv', index=False)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)