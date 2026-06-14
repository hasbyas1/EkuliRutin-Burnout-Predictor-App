import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="BurnoutCheck",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover { background-color: #388E3C; }
    html, body, p, div { font-size: 17px; }
    h1 { font-size: 2.1rem; }
    h2 { font-size: 1.6rem; }
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        text-align: center;
    }
    .section-title {
        color: #2E7D32;
        font-size: 1.2rem;
        font-weight: 600;
        border-bottom: 2px solid #A5D6A7;
        padding-bottom: 0.4rem;
        margin: 1.5rem 0 1rem 0;
    }
    
</style>
""", unsafe_allow_html=True)

# ---- LOAD MODEL ----
@st.cache_resource
def load_model():
    model = joblib.load('model_burnout_xgb_new2.pkl')
    with open('fitur_terpilih.json') as f:
        fitur = json.load(f)
    return model, fitur

model, fitur_terpilih = load_model()
label_burnout = {0: 'Low', 1: 'Moderate', 2: 'High'}

# ---- SESSION STATE ----
if 'halaman' not in st.session_state:
    st.session_state.halaman = 'landing'
if 'hasil' not in st.session_state:
    st.session_state.hasil = None

# ============================================================
# KONSTANTA PHQ-9 & GAD-7
# ============================================================
PHQ9 = [
    "Kurang tertarik atau bergairah dalam melakukan apapun",
    "Merasa sedih, tertekan, atau putus asa",
    "Sulit tidur, sering terbangun, atau tidur terlalu banyak",
    "Merasa lelah atau kurang bertenaga",
    "Kurang nafsu makan atau makan berlebihan",
    "Merasa buruk tentang diri sendiri atau merasa gagal",
    "Sulit berkonsentrasi pada sesuatu",
    "Bergerak atau berbicara lebih lambat, atau sebaliknya gelisah",
    "Muncul pikiran lebih baik mati atau ingin menyakiti diri sendiri",
]

GAD7 = [
    "Merasa gugup, cemas, atau gelisah",
    "Tidak dapat menghentikan atau mengendalikan rasa khawatir",
    "Terlalu banyak khawatir tentang berbagai hal",
    "Sulit untuk bersantai atau rileks",
    "Sangat gelisah sehingga sulit duduk diam",
    "Mudah jengkel atau mudah marah",
    "Merasa takut seolah sesuatu yang buruk akan terjadi",
]

PILIHAN = {
    "Tidak sama sekali"       : 0,
    "Beberapa hari"           : 1,
    "Lebih dari separuh waktu": 2,
    "Hampir setiap hari"      : 3,
}

# ============================================================
# HALAMAN LANDING
# ============================================================
def halaman_landing():
    st.markdown("""
    <div style='text-align:center; padding: 3rem 0 2rem 0;'>
        <div style='font-size:4rem;'>🌿</div>
        <h1 style='color:#2E7D32; font-size:2.5rem; margin-bottom:0.5rem;'>BurnoutCheck</h1>
        <p style='color:#555; font-size:1.1rem;'>Kenali tingkat risiko burnout-mu dalam 5–10 menit</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='card'>
            <div style='font-size:2rem;'>📋</div>
            <b>16 Pertanyaan Klinis</b>
            <p style='color:#777; font-size:0.85rem; margin-top:0.5rem;'>
            PHQ-9 & GAD-7 yang tervalidasi secara internasional</p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
            <div style='font-size:2rem;'>🤖</div>
            <b>Berbasis AI</b>
            <p style='color:#777; font-size:0.85rem; margin-top:0.5rem;'>
            Model XGBoost dengan akurasi 75%</p>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='card'>
            <div style='font-size:2rem;'>🔒</div>
            <b>Privasi Terjaga</b>
            <p style='color:#777; font-size:0.85rem; margin-top:0.5rem;'>
            Data tidak disimpan atau dikirim ke pihak manapun</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🌿 Mulai Assessment", use_container_width=True):
            st.session_state.halaman = 'assessment'
            st.rerun()

    st.markdown("""
    <p style='text-align:center; color:#aaa; font-size:0.82rem; margin-top:2rem;'>
    ⚠️ Aplikasi ini bukan pengganti diagnosis medis profesional dan masih dalam pengembangan.
    </p>""", unsafe_allow_html=True)

# ============================================================
# HALAMAN ASSESSMENT
# ============================================================
def halaman_assessment():
    if st.button("← Beranda"):
        st.session_state.halaman = 'landing'
        st.rerun()
    st.markdown("<h2 style='color:#2E7D32;'>📋 Assessment Burnout</h2>",
                unsafe_allow_html=True)
    st.caption("Isi semua pertanyaan berdasarkan kondisimu dalam 2 minggu terakhir.")

    with st.form("form_assessment"):

        # ---- PEKERJAAN ----
        st.markdown("<div class='section-title'>💼 Informasi Pekerjaan</div>",
                    unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            work_mode    = st.selectbox("Mode kerja", ["On-site", "Hybrid", "Remote"])
            work_hours   = st.number_input("Jam kerja per minggu",
                                           min_value=0, max_value=100, value=40)
            meetings     = st.number_input("Rata-rata meeting per hari",
                                           min_value=0, max_value=20, value=3)
        with col2:
            vacation     = st.number_input("Hari cuti yang sudah diambil tahun ini",
                                           min_value=0, max_value=365, value=0)
            uses_therapy = st.radio("Apakah kamu sedang menjalani terapi?",
                                    ["Tidak", "Ya"], horizontal=True)

        # ---- GAYA HIDUP ----
        st.markdown("<div class='section-title'>🏃 Gaya Hidup</div>",
                    unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            sleep_hours   = st.slider("Jam tidur per malam",
                                      min_value=0.0, max_value=12.0, value=7.0, step=0.5)
            exercise_days = st.slider("Hari olahraga per minggu",
                                      min_value=0, max_value=7, value=3)
        with col4:
            social_support = st.slider(
                "Seberapa besar dukungan dari orang sekitarmu?",
                min_value=1, max_value=10, value=5,
                help="1 = Sangat rendah, 10 = Sangat tinggi"
            )

        # ---- PHQ-9 ----
        st.markdown("<div class='section-title'>🧠 Kondisi Mental: PHQ-9</div>",
                    unsafe_allow_html=True)
        st.caption("Dalam **2 minggu terakhir**, seberapa sering kamu mengalami hal berikut?")
        phq9_jawaban = []
        for i, q in enumerate(PHQ9):
            jawaban = st.radio(f"{i+1}. {q}", list(PILIHAN.keys()),
                               horizontal=True, key=f"phq9_{i}")
            phq9_jawaban.append(PILIHAN[jawaban])

        # ---- GAD-7 ----
        st.markdown("<div class='section-title'>😰 Kondisi Kecemasan: GAD-7</div>",
                    unsafe_allow_html=True)
        st.caption("Dalam **2 minggu terakhir**, seberapa sering kamu mengalami hal berikut?")
        gad7_jawaban = []
        for i, q in enumerate(GAD7):
            jawaban = st.radio(f"{i+1}. {q}", list(PILIHAN.keys()),
                               horizontal=True, key=f"gad7_{i}")
            gad7_jawaban.append(PILIHAN[jawaban])

        # ---- SUBMIT ----
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍 Lihat Hasil", use_container_width=True)

        if submitted:
            phq9_score = sum(phq9_jawaban)
            gad7_score = sum(gad7_jawaban)

            input_data = pd.DataFrame([{
                'phq9_score'            : phq9_score,
                'gad7_score'            : gad7_score,
                'work_hours_per_week'   : work_hours,
                'meetings_per_day'      : meetings,
                'sleep_hours_per_night' : sleep_hours,
                'vacation_days_taken'   : vacation,
                'exercise_days_per_week': exercise_days,
                'uses_therapy'          : 1 if uses_therapy == "Ya" else 0,
                'work_mode'             : {"On-site": 0, "Hybrid": 1, "Remote": 2}[work_mode],
                'social_support_score'  : social_support,
            }])[fitur_terpilih]

            proba         = model.predict_proba(input_data)[0]
            prediksi      = int(np.argmax(proba))
            bobot         = [0, 50, 100]
            burnout_score = round(sum(p * b for p, b in zip(proba, bobot)), 2)

            st.session_state.hasil = {
                'label'      : label_burnout[prediksi],
                'score'      : burnout_score,
                'proba'      : proba.tolist(),
                'phq9_score' : phq9_score,
                'gad7_score' : gad7_score,
            }
            st.session_state.halaman = 'hasil'
            st.rerun()

# ============================================================
# HALAMAN HASIL
# ============================================================
def halaman_hasil():
    hasil  = st.session_state.hasil
    label  = hasil['label']
    score  = hasil['score']
    proba  = hasil['proba']

    cfg = {
        'Low'      : {'warna': '#2E7D32', 'bg': '#E8F5E9', 'emoji': '😊', 'teks': 'Risiko Rendah'},
        'Moderate' : {'warna': '#F57F17', 'bg': '#FFFDE7', 'emoji': '😐', 'teks': 'Risiko Sedang'},
        'High'     : {'warna': '#C62828', 'bg': '#FFEBEE', 'emoji': '😰', 'teks': 'Risiko Tinggi'},
    }
    c = cfg[label]

    # ---- RESULT BANNER ----
    st.markdown(f"""
    <div style='text-align:center; background:{c["bg"]}; border-radius:16px;
                padding:2rem; margin-bottom:1.5rem; border: 2px solid {c["warna"]}22;'>
        <div style='font-size:3.5rem;'>{c["emoji"]}</div>
        <h1 style='color:{c["warna"]}; margin:0.5rem 0;'>{c["teks"]}</h1>
        <p style='color:#555; font-size:1.1rem; margin:0;'>
            Burnout Score: <b style='color:{c["warna"]};'>{score:.2f}%</b>
        </p>
    </div>""", unsafe_allow_html=True)

    # ---- PROGRESS BAR ----
    st.markdown(f"**Burnout Score: {score:.2f}%** &nbsp; (0% = tidak burnout, 100% = sangat burnout)")
    st.progress(float(min(1.0, max(0.0, score / 100))))

    # ---- PROBABILITAS ----
    st.markdown("<br>**Distribusi Probabilitas:**", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🟢 Low",      f"{proba[0]*100:.2f}%")
    with col2:
        st.metric("🟡 Moderate", f"{proba[1]*100:.2f}%")
    with col3:
        st.metric("🔴 High",     f"{proba[2]*100:.2f}%")

    # ---- SKOR KLINIS ----
    st.markdown("<br>**Skor Klinis:**", unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    with col4:
        st.metric("PHQ-9 (Depresi)",  f"{hasil['phq9_score']} / 27")
    with col5:
        st.metric("GAD-7 (Kecemasan)", f"{hasil['gad7_score']} / 21")

    # ---- REKOMENDASI ----
    rekomen = {
        'Low': [
            "Pertahankan kebiasaan tidur dan olahraga yang baik",
            "Tetap jaga batasan waktu kerja",
            "Lakukan check-in rutin dengan diri sendiri",
        ],
        'Moderate': [
            "Pertimbangkan untuk berbicara dengan orang yang kamu percaya",
            "Evaluasi beban kerja dan prioritaskan tugas penting",
            "Tingkatkan waktu istirahat dan aktivitas yang menyenangkan",
            "Pertimbangkan konsultasi profesional jika kondisi tidak membaik",
        ],
        'High': [
            "Segera hubungi profesional kesehatan mental",
            "Bicarakan beban kerjamu dengan atasan atau HR",
            "Ambil cuti jika memungkinkan",
            "Jangan hadapi ini sendirian, minta dukungan orang terdekat",
            "📞 Into The Light Indonesia: 119",
        ],
    }

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-title'>💡 Rekomendasi</div>",
                unsafe_allow_html=True)
    for r in rekomen[label]:
        st.markdown(f"- {r}")

    # ---- TOMBOL ----
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔄 Ulangi Assessment", use_container_width=True):
            st.session_state.halaman = 'assessment'
            st.session_state.hasil   = None
            st.rerun()
    with col_b:
        if st.button("🏠 Kembali ke Beranda", use_container_width=True):
            st.session_state.halaman = 'landing'
            st.session_state.hasil   = None
            st.rerun()

    st.markdown("""
    <p style='text-align:center; color:#aaa; font-size:0.8rem; margin-top:2rem;'>
    ⚠️ Hasil ini bukan diagnosis medis. Selalu konsultasikan kondisimu dengan profesional kesehatan.
    </p>""", unsafe_allow_html=True)

# ============================================================
# ROUTING
# ============================================================
if st.session_state.halaman == 'landing':
    halaman_landing()
elif st.session_state.halaman == 'assessment':
    halaman_assessment()
elif st.session_state.halaman == 'hasil':
    halaman_hasil()