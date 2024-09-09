import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Use the model you trained in Step 7
model = best_model  # Reference the trained model variable

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

# One-hot encode the 'City' column (make sure the one-hot encoding matches your model training data)
input_data = pd.get_dummies(input_data)

# Add missing columns to match the model's training format (columns your model expects but aren't in the input)
missing_cols = set(X_train.columns) - set(input_data.columns)
for col in missing_cols:
    input_data[col] = 0

# Reorder columns to match the training data
input_data = input_data[X_train.columns]

# Make predictions using the trained model
predicted_price = model.predict(input_data)

# Display the predicted price to the user
st.write(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
