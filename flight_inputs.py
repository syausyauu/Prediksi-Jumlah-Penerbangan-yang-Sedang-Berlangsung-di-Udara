# flight_inputs.py
import streamlit as st
import numpy as np

def get_flight_inputs():
    st.header("📝 Input Data Penerbangan")
    
    month = st.slider("Bulan Keberangkatan (MONTH)", 1, 12, 1)  # default = 1
    day_of_week = st.slider("Hari dalam Minggu (DAY_OF_WEEK)", 1, 7, 7)  # default = 7
    dep_del15 = st.radio("Apakah Delay ≥15 menit sebelumnya? (DEP_DEL15)", [0, 1], index=0)  # default = 0
    
    distance_group = st.selectbox("Grup Jarak Penerbangan (DISTANCE_GROUP)", list(range(1, 11)), index=1)  # default = 2
    segment_number = st.number_input("Nomor Segmen (SEGMENT_NUMBER)", min_value=1, value=1)
    number_of_seats = st.number_input("Jumlah Kursi Pesawat (NUMBER_OF_SEATS)", min_value=1, value=143)
    
    airport_flights_month = st.number_input("Rata-rata Penerbangan Bandara/Bulan", min_value=0, value=13056)
    airline_flights_month = st.number_input("Rata-rata Penerbangan Maskapai/Bulan", min_value=0, value=107363)
    airline_airport_flights_month = st.number_input("Rata-rata Penerbangan Maskapai di Bandara", min_value=0, value=5873)
    avg_monthly_pass_airline = st.number_input("Rata-rata Penumpang Maskapai/Bulan", min_value=0, value=13382999)
    
    flt_attendants_per_pass = st.number_input("Flight Attendants per Penumpang", min_value=0.0, format="%.4f", value=6.1782)
    ground_serv_per_pass = st.number_input("Ground Service per Penumpang", min_value=0.0, format="%.4f", value=9.8894)
    plane_age = st.number_input("Usia Pesawat (tahun)", min_value=0.0, format="%.1f", value=8.0)
    tmax = st.number_input("Suhu Maksimum (TMAX °F)", format="%.1f", value=65.0)

    # Default waktu keberangkatan: Pagi
    dep_time = st.radio("Waktu Keberangkatan (DEP_TIME_BLK)", ["Subuh", "Pagi", "Siang", "Sore", "Malam"], index=1)
    dep_time_subuh, dep_time_pagi, dep_time_siang, dep_time_sore, dep_time_malam = [
        int(dep_time == lbl) for lbl in ["Subuh", "Pagi", "Siang", "Sore", "Malam"]
    ]

    return np.array([[ 
        month, day_of_week, dep_del15, distance_group, segment_number,
        number_of_seats, airport_flights_month, airline_flights_month,
        airline_airport_flights_month, avg_monthly_pass_airline,
        flt_attendants_per_pass, ground_serv_per_pass, plane_age, tmax,
        dep_time_subuh, dep_time_pagi, dep_time_siang, dep_time_sore, dep_time_malam
    ]])
