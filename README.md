# 🛡️ Network Security System - Phishing Website Detection

This project is an **AI-powered cybersecurity solution** designed to identify and block phishing websites in real-time. It reads phishing and legitimate website data from **MongoDB Atlas**, performs **feature engineering**, trains machine learning models, and exposes a user-friendly **Streamlit interface** for live predictions.

The system is built with **modular pipelines** for training and testing, enabling easy updates and evaluations on new data. It also includes pre-trained model persistence (`model.pkl`, `preprocessing.pkl`) for efficient deployment.

---

## 🚀 Project Overview

With the increasing number of phishing attacks targeting individuals and organizations, this project provides a **machine learning-based network defense mechanism** that classifies URLs as **phishing** or **legitimate** based on various attributes extracted from the URL and page structure.

**Key Functionalities:**

- 🔌 **Connects to MongoDB Atlas** for real-time access to phishing datasets  
- 🧪 **Preprocesses** and engineers features (e.g., URL length, special characters, domain info)  
- 🧠 **Trains ML models** such as Random Forest, XGBoost, and Logistic Regression  
- 🗃️ **Serializes model and preprocessing pipeline** for reuse in the UI  
- 🌐 **Streamlit Web App** to input URLs and get phishing predictions instantly  
- 📊 Evaluation pipeline with metrics such as accuracy, F1 score, and confusion matrix  

---

## 🧰 Tech Stack

| Layer              | Tools / Frameworks                    |
|-------------------|----------------------------------------|
| 💾 Data Storage     | MongoDB Atlas (Cloud NoSQL)           |
| 📥 Data Handling    | PyMongo, Pandas, NumPy                |
| 🧠 ML Framework     | Scikit-learn, XGBoost                 |
| 🔄 Pipeline Mgmt    |Pickle, Custom Training Scripts |
| 📊 Visualization    | Matplotlib                            |
| 🧪 Testing/Eval     | Scikit-learn metrics, confusion matrix |
| 🌐 UI & Serving     | Streamlit                            |
| 🐍 Language         | Python 3.0                          |

---

## 🌐 Use Case

This system can be integrated into:

- Enterprise firewalls for **real-time phishing protection**
- **Browser extensions** to warn users before opening malicious links
- **Email scanners** to flag suspicious URLs
- Educational platforms to demonstrate **cybersecurity practices**

---
