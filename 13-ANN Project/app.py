import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

## Load the trained model
model=tf.keras.models.load_model('model.h5')

## Load the encoder and scaler
with open('onehot_encoder_geo.pkl', 'rb') as file:
    label_encoder_geo = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

## Streamlit app
st.title('Customer churn Prediction App')

# User input
geography = st.selectbox('Geography', label_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', min_value=18, max_value=99)
balance = st.number_input('Balance', min_value=0)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850)
estimated_salary = st.number_input('Estimated Salary', min_value=10000, max_value=100000)
tenure = st.slider('Tenure', min_value=1, max_value=10)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4)
has_cr_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
is_active_member = st.selectbox('Is Active Member', ['Yes', 'No'])

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card == 'Yes'],
    'IsActiveMember': [is_active_member == 'Yes'],
    'EstimatedSalary': [estimated_salary]
})

# one hot encoded 'Geography'
geo_encoded = label_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=label_encoder_geo.get_feature_names_out(['Geography']))

# Combine one hot encoded columsn with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict the churn
prediction = model.predict(input_data_scaled)
prediction_prob = prediction[0][0]

if ( prediction_prob > 0.5):
    st.write(f'The customer is likely to churn with a probability of {prediction_prob*100:.2f}%')
else:
    st.write(f'The customer is not likely to churn with a probability of {prediction_prob*100:.2f}%')