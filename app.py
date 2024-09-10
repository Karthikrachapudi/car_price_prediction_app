import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model from the file
model = joblib.load('best_model.pkl')

# List of columns used during training
columns = ['City', 'Kilometers Driven', 'Fuel Type_Petrol', 'Transmission_Manual']  # Example, replace with your actual columns

# Title and description for the Streamlit app
st.title("Used Car Price Prediction App")
st.write("This application predicts the price of a used car based on its features. Provide the car details below.")

# Create input fields for user input
city = st.selectbox("Select City", ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"])
kilometers_driven = st.number_input("Enter Kilometers Driven", value=50000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Prepare input data for prediction
input_data = pd.DataFrame({
    'City': [city],
    'Kilometers Driven': [kilometers_driven],
    'Fuel Type_Petrol': [1 if fuel_type == "Petrol" else 0],
    'Transmission_Manual': [1 if transmission == "Manual" else 0]
})

# One-hot encode the 'City' column
input_data = pd.get_dummies(input_data)

# Add missing columns to match the model's training format
missing_cols = set(columns) - set(input_data.columns)
for col in missing_cols:
    input_data[col] = 0

# Reorder columns to match the training data
input_data = input_data[columns]

# Make predictions using the trained model
predicted_price = model.predict(input_data)

# Display the predicted price to the user
st.write(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
