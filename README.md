# 💳 Credit Card Fraud Detection using Machine Learning

<p align="center">

!\[Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python)
!\[Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
!\[Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge\&logo=pandas)
!\[Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=for-the-badge)
!\[CI](https://img.shields.io/github/actions/workflow/status/your-username/credit-card-fraud-detection/main.yml?style=for-the-badge)
!\[License](https://img.shields.io/badge/License-Academic-lightgrey?style=for-the-badge)

</p>

\---

## 📌 Project Overview

This project detects fraudulent credit card transactions using Machine Learning techniques.  
It addresses the challenge of **highly imbalanced data (\~0.17% fraud cases)** using SMOTE and robust evaluation metrics.

\---

## 🚀 Features

* End-to-end ML pipeline
* Data preprocessing \& feature engineering
* Multiple model comparison
* Best model selection (Random Forest)
* Streamlit web app for live predictions
* CI/CD pipeline with GitHub Actions

\---

## 📊 Dataset

* 284,807 transactions
* 30 features (V1–V28, Time, Amount)
* Target: 0 (Normal), 1 (Fraud)

\---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Imbalanced-learn (SMOTE)
* Streamlit

\---

## 🧠 Model Performance

|Model|Result|
|-|-|
|Random Forest|⭐ Best|
|Logistic Regression|Moderate|
|SVM|Poor|
|Isolation Forest|Moderate|

\---

## ▶️ Installation

```bash
git clone https://github.com/nabinduthraj/credit-card-fraud-detection.git
cd credit-card-fraud-detection
python -m venv venv
venv\\Scripts\\activate   # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

\---

## ▶️ Run Project

```bash
python src/main.py
```

### Run Web App

```bash
streamlit run app.py
```

\---

## 📁 Project Structure

```
├── data/
├── models/
├── src/
├── reports/
├── app.py
├── requirements.txt
└── README.md
```

\---

## 💼 Business Impact

* Detects fraud in real-time
* Reduces financial losses
* Improves transaction monitoring

\---

## 👨‍💻 Author

Nabin Duthraj

\---

## ⭐ Support

If you like this project, give it a star ⭐

