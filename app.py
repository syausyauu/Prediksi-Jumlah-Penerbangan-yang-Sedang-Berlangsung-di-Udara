import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Prediksi - XGBoost")

@st.cache_resource
def load_model():
    return joblib.load("xgboost_model.pkl")

model = load_model()

st.title("✈️ Prediksi Concurrent Flights (XGBoost)")

# Input sama seperti sebelumnya
month = st.slider("Bulan Keberangkatan (MONTH)", 1, 12, 1)
# Tambahkan input lainnya...

# DEP_TIME_BLK
dep_time = st.radio("Waktu Keberangkatan", ["Subuh", "Pagi", "Siang", "Sore", "Malam"])
dep_time_subuh, dep_time_pagi, dep_time_siang, dep_time_sore, dep_time_malam = [int(dep_time==lbl) for lbl in ["Subuh","Pagi","Siang","Sore","Malam"]]

# Dummy input lainnya (silakan lengkapi seperti sebelumnya)
features = np.array([[month, 1, 0, 1, 1, 100, 10000, 8000, 3000, 200000,
                      0.001, 0.002, 5.0, 75.0,
                      dep_time_subuh, dep_time_pagi, dep_time_siang, dep_time_sore, dep_time_malam]])

if st.button("Prediksi"):
    pred = model.predict(features)[0]
    st.metric("Hasil Prediksi XGBoost", f"{pred:.0f}")
