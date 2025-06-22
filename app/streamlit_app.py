import streamlit as st
import pandas as pd
from src.model_prophet import prophet_forecast

st.title("📦 Inventory Demand Forecasting")

uploaded = st.file_uploader("Upload Inventory CSV")
if uploaded:
    df = pd.read_csv(uploaded)
    forecast = prophet_forecast(df)
    st.line_chart(forecast[['ds', 'yhat']].set_index('ds'))
