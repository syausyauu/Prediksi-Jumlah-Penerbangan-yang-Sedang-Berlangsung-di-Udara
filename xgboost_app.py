import streamlit as st
import joblib
from flight_inputs import get_flight_inputs

st.set_page_config(page_title="Prediksi XGBoost", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("xgboost_model.pkl")

model = load_model()

st.title("✈️ Prediksi Concurrent Flights - XGBoost")
st.markdown("Gunakan model **XGBoost** untuk memprediksi jumlah concurrent flights berdasarkan data input.")

features = get_flight_inputs()

if st.button("🔍 Prediksi Sekarang"):
    try:
        prediction = model.predict(features)[0]
        st.success("✅ Prediksi berhasil!")
        st.metric("Hasil Prediksi", f"{prediction:.0f}")
    except Exception as e:
        st.error(f"❌ Error saat prediksi: {e}")
