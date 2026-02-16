import streamlit as st
import joblib

# -------- Page Config --------
st.set_page_config(
    page_title="Mobile Review Sentiment Analyzer",
    page_icon="📱",
    layout="wide"
)

# -------- Background Image --------
image_url = "https://t4.ftcdn.net/jpg/16/66/22/43/360_F_1666224325_mIeoiFGU1Fh8j2RFi3vqhagpvxo7BLun.jpg"

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("{image_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.sentiment-container {{
    background: rgba(0, 0, 0, 0.65);
    padding: 40px;
    border-radius: 20px;
    width: 50%;
    margin: auto;
    margin-top: 100px;
    color: white;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.6);
}}

.sentiment-container h1 {{
    text-align: center;
    margin-bottom: 30px;
}}

.stTextArea textarea {{
    background-color: rgba(255,255,255,0.9);
    border-radius: 10px;
}}

.stButton>button {{
    width: 100%;
    background-color: #ff4b4b;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 45px;
}}

</style>
""", unsafe_allow_html=True)

# -------- Load Model --------
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# -------- Overlay Container --------
st.markdown('<div class="sentiment-container">', unsafe_allow_html=True)

st.markdown("<h1>📱 Mobile Review Sentiment Analyzer</h1>", unsafe_allow_html=True)

# -------- Input --------
user_input = st.text_area("Enter Mobile Review")

# -------- Prediction --------
if st.button("Analyze Sentiment"):
    if user_input.strip() != "":
        vector = tfidf.transform([user_input])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.success("✅ Sentiment: Positive 😊")
        else:
            st.error("❌ Sentiment: Negative 😞")
    else:
        st.warning("⚠ Please enter a review first.")

st.markdown('</div>', unsafe_allow_html=True)

