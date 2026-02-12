import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Title
st.title("📱 Mobile Review Sentiment Analyzer")

# Text input
user_input = st.text_area("Enter Review")

# Button + Prediction Logic
if st.button("Analyze Sentiment"):
    if user_input.strip() != "":
        vector = tfidf.transform([user_input])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.success("Sentiment: Positive 😊")
        else:
            st.error("Sentiment: Negative 😞")
    else:
        st.warning("Please enter a review first.")
