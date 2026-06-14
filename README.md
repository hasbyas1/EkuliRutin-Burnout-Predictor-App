# 🌿 EkuliRutin | Aplikasi Prediksi Risiko Burnout

COBA APLIKASINYA DI SINI! <br>
[![Streamlit App](https://img.shields.io/badge/Streamlit-Open%20App-FF4B4B?logo=streamlit&logoColor=white)](https://ekulirutin.streamlit.app)

Presentasi Aplikasi: <br>
[![YouTube](https://img.shields.io/badge/YouTube-Presentation%20Video-FF0000?logo=youtube&logoColor=white)](https://youtu.be/pZqv8l8R4_g)

Tutorial Penggunaan Aplikasi (bukan setup): <br>
[![YouTube](https://img.shields.io/badge/YouTube-Demo%20Video-FF0000?logo=youtube&logoColor=white)](https://youtu.be/nn7vj3JV9Yg)

---

Aplikasi web berbasis AI untuk mendeteksi risiko burnout secara dini melalui asesmen mandiri menggunakan instrumen klinis PHQ-9, GAD-7, dan data perilaku kerja sehari-hari.

Proyek ini berfokus pada pengembangan sistem asisten produktivitas berbasis kecerdasan buatan yang dirancang untuk membantu individu mengelola waktu dan aktivitas harian secara lebih efektif dan terstruktur. Dengan menerapkan model supervised learning, sistem akan menganalisis berbagai metrik gaya hidup, seperti durasi tidur, jam kerja, dan tingkat stres, untuk memprediksi probabilitas terjadinya kelelahan ekstrem (burnout) secara dini.

## Fitur
- Asesmen 5–10 menit dengan antarmuka langkah demi langkah
- Instrumen klinis tervalidasi: PHQ-9 (depresi) & GAD-7 (kecemasan)
- Hasil berupa level risiko (Low / Moderate / High) + burnout score 0–100%
- Rekomendasi tindak lanjut berdasarkan hasil

## Model
- Algoritma  : XGBoost Classifier
- Akurasi    : 75.3% (F1 Macro: 0.74)
- Fitur input : 10 fitur (PHQ-9, GAD-7, jam kerja, tidur, dll.)
- Kelas target: Low · Moderate · High

> Model dilatih secara terpisah di repositori
> [![GitHub](https://img.shields.io/badge/GitHub-EkulitRutin%20App-181717?logo=github&logoColor=white)](https://github.com/hasbyas1/EkuliRutin-Train.git)
> Hanya file model (`.pkl`) dan metadata (`.json`) yang disertakan di sini.

## Menjalankan Secara Lokal

### Prasyarat
- Python 3.9 atau lebih baru
- pip

### Langkah-langkah

**1. Clone repositori**
```bash
git clone https://github.com/hasbyas1/EkuliRutin-Burnout-Predictor-App.git
cd EkuliRutin-Burnout-Predictor-App
```

**2. Buat virtual environment (opsional tapi disarankan)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi**
```bash
streamlit run app.py
```

**5. Buka di browser**

Streamlit akan otomatis membuka browser. Jika tidak, buka manual:
```
http://localhost:8501
```

## Deploy ke Streamlit Cloud

1. Push repo ini ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Klik **New app** → pilih repo ini → set `app.py` sebagai main file
4. Klik **Deploy**

## Struktur File
burnout-predictor-app/ <br>
├── app.py <br>
├── model_burnout_xgb_new2.pkl <br>
├── fitur_terpilih.json <br>
├── label_burnout.json <br>
├── requirements.txt <br>
└── README.md <br>

## Disclaimer
Aplikasi ini bersifat edukatif dan **bukan pengganti diagnosis medis
profesional**. Jika kamu mengalami gejala burnout yang serius,
segera konsultasikan dengan tenaga kesehatan mental.

---

## DICODING | CAPSTONE PROJECT
**AIC117B6Y0044 | Muhammad Hasby As-shiddiqy**
