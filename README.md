# 📱 Mobile Price Predictor

🚀 [Click here to try the live app](https://abeth23-mobile-price-predictor-app-mbyrx2.streamlit.app/)

A machine learning-powered **Streamlit web app** that predicts the price of a mobile phone based on its specifications like brand, model, RAM, storage, and battery capacity.

---

## 💡 Features

- 🔍 Predicts mobile prices using a trained ML model
- 📦 Inputs include:
  - Brand
  - Model
  - RAM (GB)
  - Storage (GB)
  - Battery Capacity (mAh)
- 🎯 Uses log-transformed regression to estimate accurate prices
- 🖥️ Clean and responsive Streamlit UI

---

## 🛠️ Tech Stack

| Category       | Tools / Libraries                      |
|----------------|----------------------------------------|
| Frontend       | Streamlit                              |
| Backend        | Python                                 |
| Machine Learning | scikit-learn, XGBoost (optional)       |
| Data Handling  | pandas, numpy                          |
| Deployment     | Streamlit Cloud                        |

---

## 🗂️ Project Structure

├── app.py # Main Streamlit app
├── pipe.pkl # Trained ML pipeline
├── df.pkl # DataFrame for dropdown values
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
