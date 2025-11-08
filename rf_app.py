import streamlit as st
import joblib
from flight_inputs import get_flight_inputs

st.set_page_config(page_title="Prediksi Random Forest", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("random_forest_best_model.pkl")

model = load_model()

st.title("✈️ Prediksi Concurrent Flights - Random Forest")
st.markdown("Gunakan model **Random Forest** untuk memprediksi jumlah concurrent flights berdasarkan data input.")

features = get_flight_inputs()

if st.button("🔍 Prediksi Sekarang"):
    try:
        prediction = model.predict(features)[0]
        st.success("✅ Prediksi berhasil!")
        st.metric("Hasil Prediksi", f"{prediction:.0f}")
    except Exception as e:
        st.error(f"❌ Error saat prediksi: {e}")
