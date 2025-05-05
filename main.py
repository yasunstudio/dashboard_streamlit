import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# DATA
data_bendungan = pd.DataFrame({
    'tanggal': pd.date_range('2025-01-01', periods=5).tolist() * 2,
    'lokasi': ['Bendungan A'] * 5 + ['Bendungan B'] * 5,
    'debit_air_m3s': [310, 320, 315, 300, 290, 280, 270, 265, 275, 285]
})

data_plta = pd.DataFrame({
    'tanggal': pd.date_range('2025-01-01', periods=5).tolist() * 2,
    'nama_plta': ['PLTA A'] * 5 + ['PLTA B'] * 5,
    'produksi_mwh': [1500, 1520, 1490, 1510, 1505, 1300, 1315, 1290, 1280, 1320]
})

# JUDUL
st.title("Dashboard Monitoring Bendungan dan PLTA")

# PILIHAN FILTER
lokasi_bendung = st.selectbox("Pilih Bendungan", data_bendungan['lokasi'].unique())
plta_terpilih = st.selectbox("Pilih PLTA", data_plta['nama_plta'].unique())

# FILTER DATA
data_bendungan_filter = data_bendungan[data_bendungan['lokasi'] == lokasi_bendung]
data_plta_filter = data_plta[data_plta['nama_plta'] == plta_terpilih]

# TAMPILKAN TABEL
st.subheader(f"Data Debit Air - {lokasi_bendung}")
st.dataframe(data_bendungan_filter)

st.subheader(f"Data Produksi Listrik - {plta_terpilih}")
st.dataframe(data_plta_filter)

# VISUALISASI GRAFIK
st.subheader("Grafik Debit Air")
fig, ax = plt.subplots()
ax.plot(data_bendungan_filter['tanggal'], data_bendungan_filter['debit_air_m3s'], marker='o')
ax.set_ylabel("Debit (m³/s)")
ax.set_xlabel("Tanggal")
ax.set_title(f"Debit Air Harian - {lokasi_bendung}")
st.pyplot(fig)

st.subheader("Grafik Produksi Listrik")
fig2, ax2 = plt.subplots()
ax2.plot(data_plta_filter['tanggal'], data_plta_filter['produksi_mwh'], color='green', marker='o')
ax2.set_ylabel("Produksi (MWh)")
ax2.set_xlabel("Tanggal")
ax2.set_title(f"Produksi Harian - {plta_terpilih}")
st.pyplot(fig2)
