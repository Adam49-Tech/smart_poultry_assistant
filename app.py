import streamlit as st
from PIL import Image
import os
from utils.breed_predictor import predict_breed
from utils.feed_calculator import calculate_feed
from utils.disease_predictor import SYMPTOM_COLS, predict_disease
from utils.price_predictor import estimate_price
from utils.biosecurity_advice import get_biosecurity_tip
from utils.treatment_advice import get_treatment
from database.db_handler import create_table, insert_record
# Ensure table exists
create_table()
st.set_page_config(page_title="Smart Poultry Assistant", layout="wide")
st.title("🐔 Smart Poultry Assistant")
# Tabs
tabs = st.tabs(["📷 Breed Prediction", "🧪 Disease Predictor", "🧮 Feed Calculator",
                 "💰 Price Estimator", "🛡️ Biosecurity Tips", "📋 View Records"])
# --- Breed Predictor Tab ---
with tabs[0]:
    st.subheader("📷 Poultry Breed Prediction")
    uploaded_file = st.file_uploader("Upload a chicken image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        if st.button("Predict Breed"):
            breed, breed_name = predict_breed(image)
            st.success(f"Predicted Breed = {breed} - {breed_name}")
            input_data = uploaded_file.name
            insert_record("Breed Prediction", input_data, f"{breed} - {breed_name}")
            st.success("📥 Prediction saved to records.")
# --- Disease Predictor Tab ---
with tabs[1]:
    st.subheader("🧪 Poultry Disease Predictor")
    selected_symptoms = st.multiselect("Select observed symptoms:", SYMPTOM_COLS)
    if st.button("Predict Disease"):
        if selected_symptoms:
            prediction, treatment = predict_disease(selected_symptoms)
            st.success(f"🦠 Predicted Disease: {prediction}")
            st.info(f"💊 Suggested Treatment: {treatment}")
            # Convert list to string and save to DB
            symptom_str = ", ".join(selected_symptoms)
            insert_record("Disease Predictor", symptom_str, prediction, treatment)
            st.success("📥 Prediction saved to records.")
        else:
            st.warning("Please select at least one symptom.")
# --- Feed Calculator Tab ---
with tabs[2]:
    st.subheader("🧮 Feed Calculator")
    bird_type = st.selectbox("Select bird type:", ["Broiler", "Layer", "Cockerel"])
    age_days = st.number_input("Enter bird age (in days):", min_value=1, step=1)
    num_birds = st.number_input("Enter number of birds:", min_value=1, step=1)
    feed_type = st.selectbox("Select type of feed:", ["Starter", "Grower", "Finisher", "Super Starter"])
    if st.button("Calculate Feed"):
        feed_amount = calculate_feed(bird_type, age_days, num_birds, feed_type)
        if isinstance(feed_amount, str):
            st.error(feed_amount)
        else:
            st.success(f"Recommended Feed: {feed_amount:.2f} kg")
            input_summary = f"{num_birds} {bird_type}s, {age_days} days, {feed_type}"
            insert_record("Feed Calculator", input_summary, f"{feed_amount:.2f} kg")
            st.success("📥 Record saved.")
# --- Price Estimator Tab ---
with tabs[3]:
    st.subheader("💰 Price Estimator")
    bird_type = st.selectbox("Select bird type:", ["Broiler", "Layer", "Cockerel"], key="price")
    age_weeks = st.number_input("Enter bird age (in weeks):", min_value=1, step=1)
    if st.button("Estimate Price"):
        price = estimate_price(bird_type, age_weeks)
        st.success(f"Estimated Price: ₦{price}")
        input_str = f"{bird_type} - {age_weeks} weeks"
        insert_record("Price Estimator", input_str, f"₦{price}")
        st.success("📥 Record saved.")
# --- Biosecurity Tips Tab ---
with tabs[4]:
    st.subheader("🛡️ Biosecurity Tips")
    challenge = st.selectbox("Select farm challenge:", [
        "High mortality", "Disease outbreak", "Low egg production",
        "Slow growth", "Poor feed conversion", "Wet litter",
        "Foul odor", "Parasite infestation"])
    if st.button("Get Biosecurity Tip"):
        tip = get_biosecurity_tip(challenge)
        st.info(f"💡 Tip: {tip}")
        insert_record("Biosecurity Tips", challenge, tip)
        st.success("📥 Tip saved to records.")
# --- View Records Tab ---
with tabs[5]:
    st.subheader("📋 View Saved Records")
    import sqlite3
    import pandas as pd
    conn = sqlite3.connect("poultry_records.db")
    df = pd.read_sql_query("SELECT * FROM records ORDER BY timestamp DESC", conn)
    conn.close()
    st.dataframe(df)
    if not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Records as CSV",
            data=csv,
            file_name="poultry_records.csv",
            mime="text/csv"
        )
