import streamlit as st
import pandas as pd
import numpy as np

def tampilkan_visualisasi():
    st.title("📊 Visualisasi Fitur Data Pelanggan")
    st.markdown("#### Simulasi data pelanggan untuk ilustrasi")

    np.random.seed(42)
    data = pd.DataFrame({
        'Tenure': np.random.randn(100).cumsum(),
        'MonthlyCharges': np.random.randn(100).cumsum(),
        'TotalCharges': np.random.randn(100).cumsum()
    })

    st.subheader("🎛️ Filter Range Data")
    range_val = st.slider("Pilih range baris:", 0, len(data)-1, (25, 75))
    st.write(f"Menampilkan data dari baris: {range_val}")

    filtered = data.iloc[range_val[0]:range_val[1]]
    st.line_chart(filtered)
