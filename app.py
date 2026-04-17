import streamlit as st
import numpy as np
import pickle
import os
import requests

st.set_page_config(page_title="Trader Intelligence Dashboard", layout="wide")

# =========================
# DOWNLOAD FUNCTION (FAST + SAFE)
# =========================
def download_file(file_id, filename):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    try:
        with st.spinner(f"Downloading {filename}..."):
            r = requests.get(url, stream=True, timeout=30)
            r.raise_for_status()

            with open(filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024*1024):  # 1MB chunks
                    if chunk:
                        f.write(chunk)

    except Exception as e:
        st.error(f"❌ Failed to download {filename}")
        st.stop()

# =========================
# FILE IDS (KEEP ONLY IMPORTANT ONES)
# =========================
MODEL_FILES = {
    "model.pkl": "1yP2jCXFZE9gRUiIAng2Hz-_i6waizFIt",
    "scaler.pkl": "1EQ_Oih0m6YPHCNEA8QroQbqmid2byuNY",
    "features.pkl": "1_j8DHLsOc74LTp2Rp3NGU6BjCLj2s7c7"
}

# =========================
# LOAD MODELS (CACHED)
# =========================
@st.cache_resource
def load_models():
    st.write("🚀 Loading models...")

    for file, file_id in MODEL_FILES.items():
        if not os.path.exists(file):
            st.write(f"📥 Downloading {file}")
            download_file(file_id, file)
        else:
            st.write(f"✅ Found {file}")

    model = pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    features = pickle.load(open("features.pkl", "rb"))

    return model, scaler, features

try:
    model, scaler, features = load_models()
except:
    st.error("❌ Model loading failed")
    st.stop()

# =========================
# UI
# =========================
st.title("📊 Trader Intelligence Dashboard")
st.caption("Behavioral + Sentiment-driven trading analytics")

st.subheader("🔮 Trade Outcome Prediction")

inputs = []

for f in features:
    if f == "is_long":
        val = st.selectbox("Trade Type", ["Short (Sell)", "Long (Buy)"])
        val = 1 if val == "Long (Buy)" else 0

    elif f == "sentiment":
        val = st.selectbox("Market Sentiment", ["Fear", "Neutral", "Greed"])
        val = {"Fear": 0, "Neutral": 0.5, "Greed": 1}[val]

    else:
        val = st.number_input(f.replace("_", " ").title(), value=0.0)

    inputs.append(val)

# =========================
# PREDICTION
# =========================
if st.button("Predict Trade Outcome"):

    try:
        arr = scaler.transform(np.array(inputs).reshape(1, -1))
        pred = model.predict(arr)[0]

        if pred == 1:
            st.success("✅ Profitable Trade")
        else:
            st.error("❌ Loss Making Trade")

    except Exception as e:
        st.error("⚠️ Prediction failed. Feature mismatch.")

# =========================
# FOOTER
# =========================
st.sidebar.markdown("---")
st.sidebar.write("Harshita Sharma • ML Project")