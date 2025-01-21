import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load the trained model
# Ensure you have saved your trained model as a pickle file, e.g., "flight_fare_model.pkl"
with open("rf_reg.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("Flight Fare Prediction")

# User inputs
st.header("Enter Flight Details:")

# Total Stops
total_stops = st.selectbox("Number of Stops", [0, 1, 2, 3, 4])

# Duration
duration_hrs = st.number_input("Duration (Hours)", min_value=0, max_value=24, value=1, step=1)
duration_mins = st.number_input("Duration (Minutes)", min_value=0, max_value=59, value=0, step=1)

# Date of Journey
day_of_journey = st.number_input("Day of Journey", min_value=1, max_value=31, value=1, step=1)
month_of_journey = st.number_input("Month of Journey", min_value=1, max_value=12, value=1, step=1)

# Departure Time
dep_hr = st.number_input("Departure Hour", min_value=0, max_value=23, value=0, step=1)
dep_min = st.number_input("Departure Minute", min_value=0, max_value=59, value=0, step=1)

# Arrival Time
arrival_hr = st.number_input("Arrival Hour", min_value=0, max_value=23, value=0, step=1)
arrival_min = st.number_input("Arrival Minute", min_value=0, max_value=59, value=0, step=1)

# Airline Selection
airlines = [
    "Air India", "GoAir", "IndiGo", "Jet Airways", "Jet Airways Business", "Multiple carriers",
    "Multiple carriers Premium economy", "SpiceJet", "Trujet", "Vistara", "Vistara Premium economy"
]
selected_airline = st.selectbox("Airline", airlines)

# Source Selection
sources = ["Chennai", "Delhi", "Kolkata", "Mumbai"]
selected_source = st.selectbox("Source", sources)

# Destination Selection
destinations = ["Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"]
selected_destination = st.selectbox("Destination", destinations)

# One-hot encode categorical inputs
airline_features = [1 if selected_airline == f"Airline_{airline}" else 0 for airline in airlines]
source_features = [1 if selected_source == f"Source_{source}" else 0 for source in sources]
destination_features = [1 if selected_destination == f"Destination_{destination}" else 0 for destination in destinations]

# Combine all inputs into a single feature array
input_features = [
    total_stops, duration_hrs, duration_mins, day_of_journey, month_of_journey,
    dep_hr, dep_min, arrival_hr, arrival_min
] + airline_features + source_features + destination_features

# Prediction
if st.button("Predict Fare"):
    prediction = model.predict([input_features])
    st.success(f"The predicted flight fare is ₹{prediction[0]:,.2f}")
