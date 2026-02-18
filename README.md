📱 Mobile Review Sentiment Analyzer
📌 Project Overview

The Mobile Review Sentiment Analyzer is a Machine Learning web application that classifies customer mobile phone reviews as Positive or Negative using Natural Language Processing (NLP).

The application is built using:

Python

Scikit-Learn

TF-IDF Vectorization

Streamlit (for deployment UI)

It allows users to input a mobile product review and instantly receive a sentiment prediction.

🎯 Problem Statement

Customer reviews play a crucial role in product improvement and brand perception. However, manually analyzing large volumes of reviews is time-consuming and inefficient.

This project automates sentiment classification using NLP techniques to help businesses quickly understand customer feedback.

🗂 Dataset

File: Mobile Reviews Sentiment.csv

Contains mobile product reviews labeled as:

1 → Positive

0 → Negative

The dataset was used for:

Data Cleaning

Text Preprocessing

Feature Extraction

Model Training

⚙️ Project Workflow

Data Understanding

Loaded dataset

Performed exploratory data analysis

Text Preprocessing

Lowercasing

Removing punctuation

Removing stopwords

Cleaning special characters

Feature Engineering

Applied TF-IDF Vectorization

Converted text into numerical vectors

Model Training

Trained classification model using Scikit-Learn

Saved trained model as:

sentiment_model.pkl

tfidf_vectorizer.pkl

Deployment

Built interactive UI using Streamlit

Integrated trained model for real-time predictions

🖥 Application Features

Clean and modern UI

Background styling

Real-time sentiment prediction

User-friendly text input

Instant Positive/Negative output

📁 Project Structure
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── Mobile Reviews Sentiment.csv
├── data_understanding.ipynb
└── README.md

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone <your-repository-link>
cd <your-repository-name>

2️⃣ Install Required Libraries
pip install -r requirements.txt


(If no requirements file, install manually:)

pip install streamlit scikit-learn pandas numpy joblib

3️⃣ Run the Application
streamlit run app.py


The app will open in your browser.

📊 Model Details

Vectorizer: TF-IDF

Algorithm: Machine Learning Classifier (Scikit-Learn)

Output Classes: Positive (1) / Negative (0)

🔮 Future Improvements

Add Neutral sentiment classification

Improve model accuracy using deep learning (LSTM / BERT)

Deploy on Streamlit Cloud / Heroku

Add model accuracy metrics display

Add visualization dashboard

👩‍💻 Author

Vijaya Jyothi Nersu
Machine Learning & Data Science Enthusiast
