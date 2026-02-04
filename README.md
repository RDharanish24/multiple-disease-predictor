# 🏥 Multiple Disease Prediction System

A Machine Learning–based web application that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Breast Cancer** using pre-trained models.  
The application is built using **Streamlit** for an interactive user interface and **scikit-learn** for model predictions.

---

## 🚀 Features

- 🩸 **Diabetes Prediction**
- ❤️ **Heart Disease Prediction**
- 🎗️ **Breast Cancer Prediction**
- User-friendly web interface
- Sidebar navigation using option menu
- Real-time predictions using trained ML models

---

## 🗂️ Project Structure

```
Multiple-Disease-Prediction/
│
├── models/
│ ├── trained_model.sav
│ ├── heartdiseasemodel.sav
│ └── breastcancermodel.sav
│
├── multipledisease.py
├── requirements.txt
└── README.md

```
---

## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **scikit-learn**
- **NumPy**
- **Pickle**
- **streamlit-option-menu**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/RDharanish24/multiple-disease-prediction.git
cd multiple-disease-prediction
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```
3️⃣ Run the application
```
streamlit run multipledisease.py
```

---
## 🧪 How It Works
- User selects a disease from the sidebar menu.

- Enters the required medical parameters.

- The input data is passed to the respective trained ML model.

- The model predicts the disease outcome.

- Result is displayed instantly on the screen.

## 📌 Note
- This project is intended for educational purposes only.

- The predictions should not be used for medical diagnosis.

- Ensure the models folder remains in the same directory as the main Python file.