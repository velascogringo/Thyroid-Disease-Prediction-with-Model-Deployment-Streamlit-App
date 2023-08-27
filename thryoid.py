import streamlit as st
import joblib

# Load the trained model
model = joblib.load('thyroid_model.sav')

# Streamlit UI
st.title('Thyroid Disease Prediction')
st.write('Input the following features to get a prediction:')

# Input fields
age = st.number_input('Age', min_value=1, max_value=100, value=25)
gender = st.selectbox('Gender', ['Male', 'Female'])
tsh = st.number_input('TSH', min_value=0.01, max_value=100.0, value=1.0)
t3 = st.number_input('T3', min_value=0.1, max_value=10.0, value=2.0)
tt4 = st.number_input('TT4', min_value=1.0, max_value=500.0, value=100.0)

# Convert gender to numeric (assuming Male=0, Female=1)
gender_num = 1 if gender == 'Female' else 0

# Prepare input features for prediction
input_features = [[age, gender_num, tsh, t3, tt4]]

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_features)
    if prediction == 0:
        st.write('Prediction: No Thyroid Disease')
    else:
        st.write('Prediction: Thyroid Disease Detected')
