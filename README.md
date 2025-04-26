🚀 Portfolio Streamlit - Data Scientist 
Halo! Ini adalah web portfolio saya yang dibangun menggunakan Streamlit.
Di sini Anda bisa melihat tentang saya, proyek-proyek yang saya buat, serta beberapa eksperimen machine learning sederhana.

📂 Struktur Project
bash
Copy
Edit
BELAJAR_STREAMLIT/
│
├── app.py                # Main aplikasi Streamlit
├── About_me.py           # Halaman Tentang Saya
├── kontak.py             # Halaman Kontak (LinkedIn & GitHub)
├── visualisasi.py        # Halaman Visualisasi Data
├── prediksi.py           # Halaman Prediksi Churn (Machine Learning)
│
├── bank_churn_data.csv   # Dataset bank churn untuk visualisasi
├── X_test.csv            # Data testing untuk prediksi
├── y_test.csv            # Label testing untuk prediksi
├── xgb_model.joblib      # Model XGBoost untuk prediksi
│
├── env-streamlit/        # Virtual environment (tidak perlu upload)
├── __pycache__/          # Cache Python (abaikan)
│
└── README.md             # Dokumentasi project ini
⚙️ Cara Menjalankan Project
Clone repo ini:

bash
Copy
Edit
git clone https://github.com/username-kamu/portfolio-streamlit.git
cd portfolio-streamlit
Aktifkan environment:

bash
Copy
Edit
.\env-streamlit\Scripts\activate
Install requirements:

bash
Copy
Edit
pip install -r requirements.txt
Jalankan aplikasi:

bash
Copy
Edit
streamlit run app.py
🖥️ Fitur Aplikasi
Tentang Saya: Menampilkan profil singkat dan bidang keahlian saya.

Proyek: Menampilkan visualisasi data.

Machine Learning: Prediksi apakah pelanggan akan churn menggunakan model XGBoost.

Kontak: Terhubung dengan saya lewat LinkedIn dan GitHub.

🛠️ Teknologi yang Digunakan
Python 3.12

Streamlit

Scikit-learn

XGBoost

Pandas

Matplotlib

Scikit-plot

LIME (Local Interpretable Model-agnostic Explanations)

DALEX (Model explanation tools)

📬 Kontak Saya
LinkedIn: LinkedIn Saya

GitHub: GitHub Saya

📄 Lisensi
Project ini dibuat untuk tujuan pembelajaran dan personal branding.
Bebas digunakan untuk referensi pribadi.
