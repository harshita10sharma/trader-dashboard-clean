# Trader Intelligence Dashboard

A data-driven machine learning application that analyzes trader behavior based on market sentiment (Fear vs Greed) and predicts trading outcomes.

---

## Live Application

https://trader-dashboard-clean-ekzsmic8vy7kypzkk72x9u.streamlit.app/

---

## Objective

To understand how market sentiment influences trader decisions and profitability, and to build predictive models that assist in better trading strategies.

---

## Dataset

- Bitcoin Fear & Greed Index  
- Hyperliquid Trader Data  

---

## Features

### 1. Trade Outcome Prediction
Predicts whether a trade will be profitable based on:
- Trade size  
- Trade direction (Long / Short)  
- Market sentiment (Fear / Greed)  
- Historical trader behavior  

---

### 2. Next-Day Profitability Prediction
Classifies expected trader performance into:
- Loss  
- Neutral  
- Profit  

---

### 3. Trader Clustering
Segments traders into behavioral groups:
- Conservative  
- Aggressive  
- High-frequency  

---

## Models Used

- Random Forest Classifier  
- KMeans Clustering  
- StandardScaler (feature normalization)  

---

## Tech Stack

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## Key Insights

- High greed sentiment often leads to higher returns but increased risk  
- High-frequency trading tends to reduce overall win rate  
- Larger trade sizes do not guarantee profitability  

---

## Deployment Strategy

Model files are not stored in GitHub due to size constraints.

Instead:
- Models are hosted on Google Drive  
- Files are downloaded dynamically at runtime  
- This ensures lightweight repository and faster deployment  

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py