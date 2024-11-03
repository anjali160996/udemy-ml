import streamlit as st
import pandas as pd
import numpy as np

## Title of app
st.title('Data Analysis App')

## Display a simple text
st.write('This app will help you perform basic data analysis on a given dataset.')

## Create a simple Dataframe

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 28, 35, 22],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Berlin']
})

## Display the dataframe
st.write('Dataframe:')
st.dataframe(df)


## create a line chart
st.line_chart(df['Age'], df['City'])