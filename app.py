import streamlit as st
import numpy as np
import joblib

# Load model (save your trained model first as model.pkl)
model = joblib.load("models/model.pkl")

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check if it's fraudulent.")

# Example inputs (simplified)
amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.number_input("Transaction Time", min_value=0.0)

# Dummy inputs for V1–V28
features = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    features.append(val)

if st.button("Predict"):
    data = np.array([time, amount] + features).reshape(1, -1)
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")
