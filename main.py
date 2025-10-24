import streamlit as st
import pandas as pd
import joblib

# Load the pipeline
model = joblib.load("1_final_model.pkl")

st.set_page_config(page_title="Gemstone Price Predictor", layout="centered")

st.title("Gemstone Price Prediction App")
st.markdown("Predict the **price of a diamond** based on its characteristics.")

# --- USER INPUT SECTION ---

st.header("Enter Diamond Details")

col1, col2 = st.columns(2)

with col1:
    carat = st.slider("Carat Weight", 0.2, 5.0, 1.0, step=0.01)
    depth = st.slider("Depth (%)", 55.0, 70.0, 61.5, step=0.1)
    table = st.slider("Table (%)", 50.0, 70.0, 57.0, step=0.1)
    x = st.slider("X (mm)", 3.0, 10.0, 5.0, step=0.01)
    
with col2:
    y = st.slider("Y (mm)", 3.0, 10.0, 5.0, step=0.01)
    z = st.slider("Z (mm)", 2.0, 7.0, 3.0, step=0.01)

    # Dropdowns for categorical values
    cut = st.selectbox("Cut", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox("Color", ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox("Clarity", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

# --- PREDICTION SECTION ---
st.markdown("---")
if st.button(" Predict Price"):
    # Create input dataframe
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    st.success(f"### 💎 Estimated Diamond Price: **${prediction:,.2f}**")

st.markdown("---")
