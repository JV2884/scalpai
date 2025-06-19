# App updated with new model
import streamlit as st
from PIL import Image
import random
st.info("✅ Using model: scalpai_model.h5 (trained version)")

st.set_page_config(page_title="ScalpAI", layout="centered")
st.title("📈 ScalpAI - 1-Min Chart Predictor")
st.write("Upload a 1-minute chart (60 candles), and get a prediction:")

uploaded_file = st.file_uploader("Upload your chart screenshot", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chart", use_column_width=True)

    # 🔮 Mock prediction (will replace with AI model)
    prediction = random.choice(["📈 UP - Buy", "📉 DOWN - Sell"])
    st.subheader("Prediction:")
    st.success(prediction)
