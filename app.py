import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page title
st.title("🌍 World Development Cluster Prediction")
st.write("Enter the development indicators below to predict the country's cluster.")

# Features used for clustering
features = [
    "Birth Rate",
    "Business Tax Rate",
    "CO2 Emissions",
    "Days to Start Business",
    "Energy Usage",
    "GDP",
    "Health Exp % GDP",
    "Health Exp/Capita",
    "Hours to do Tax",
    "Infant Mortality Rate",
    "Internet Usage",
    "Lending Interest",
    "Life Expectancy Female",
    "Life Expectancy Male",
    "Mobile Phone Usage",
    "Population 0-14",
    "Population 15-64",
    "Population 65+",
    "Population Total",
    "Population Urban",
    "Tourism Inbound",
    "Tourism Outbound"
]

# Collect user inputs
values = []

for feature in features:
    value = st.number_input(
        feature,
        value=0.0
    )
    values.append(value)

# Prediction button
if st.button("Predict Cluster"):

    # Convert input into DataFrame
    input_data = pd.DataFrame([values], columns=features)

    # Scale the input using the saved scaler
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f"Predicted Cluster: {cluster}")