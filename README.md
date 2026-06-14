# 🌿 EkuliRutin — Aplikasi Prediksi Risiko Burnout

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://burnoutcheck.streamlit.app)

Aplikasi web berbasis AI untuk mendeteksi risiko burnout secara dini
melalui asesmen mandiri menggunakan instrumen klinis PHQ-9, GAD-7,
dan data perilaku kerja sehari-hari.

## ✨ Fitur
- Asesmen 5–10 menit dengan antarmuka langkah demi langkah
- Instrumen klinis tervalidasi: PHQ-9 (depresi) & GAD-7 (kecemasan)
- Hasil berupa level risiko (Low / Moderate / High) + burnout score 0–100%
- Rekomendasi tindak lanjut berdasarkan hasil

## 🤖 Model
- Algoritma  : XGBoost Classifier
- Akurasi    : 75.3% (F1 Macro: 0.74)
- Fitur input : 10 fitur (PHQ-9, GAD-7, jam kerja, tidur, dll.)
- Kelas target: Low · Moderate · High

> Model dilatih secara terpisah di repositori
> [burnout-predictor-training](#).
> Hanya file model (`.pkl`) dan metadata (`.json`) yang disertakan di sini.

## 🚀 Menjalankan Secara Lokal

```bash
git clone https://github.com/hasbyas1/EkuliRutin-Burnout-Predictor-App.git
cd EkuliRutin-Burnout-Predictor-App
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy ke Streamlit Cloud

1. Push repo ini ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Klik **New app** → pilih repo ini → set `app.py` sebagai main file
4. Klik **Deploy**

## 📁 Struktur File
burnout-predictor-app/
├── app.py
├── model_burnout_xgb_final.pkl
├── fitur_terpilih.json
├── label_burnout.json
├── requirements.txt
└── README.md

## ⚠️ Disclaimer
Aplikasi ini bersifat edukatif dan **bukan pengganti diagnosis medis
profesional**. Jika kamu mengalami gejala burnout yang serius,
segera konsultasikan dengan tenaga kesehatan mental.

---

## DICODING — CAPSTONE PROJECT
**AIC117B6Y0044 — Muhammad Hasby As-shiddiqy**