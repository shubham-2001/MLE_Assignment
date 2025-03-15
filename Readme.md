# **🏡 House Price Prediction API**



📢 **An end-to-end machine learning application** that predicts house prices based on various features. The project covers **data preprocessing, model training, hyperparameter tuning, API deployment using Flask, Dockerization, and Cloud Deployment**.  

---

## 📌 **Project Overview**
This repository contains:
- **Jupyter Notebook** (`MLE_Assignment.ipynb`) for data analysis, feature engineering, model training, and tuning.
- **Flask API** (`app.py`) for serving predictions.
- **Model files** (`best_rf_model.pkl`, `scaler.pkl`) for inference.
- **Dockerfile** for containerizing the application.
- **README.md** (this file) explaining the setup and execution.
- **requirements.txt** listing the necessary dependencies.

---

## 🎯 **Key Features**
✔️ **Data Preprocessing & Feature Engineering**  
✔️ **Machine Learning Model Training & Hyperparameter Tuning** (RandomForest, XGBoost)  
✔️ **Model Versioning** (DVC/MLflow)  
✔️ **Logging & Error Handling in Flask API**  
✔️ **RESTful API using Flask**  
✔️ **Docker Support**  
✔️ **Cloud Deployment (AWS, GCP, Azure, Render)**  
✔️ **Simple Front-End for User Interaction**  

---

## 📦 **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/shubham-2001/MLE_Assignment.git
cd MLE_Assignment
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 📊 **Data & Model Training**
1. **Open Jupyter Notebook**:
2. **Run** the `MLE_Assignment.ipynb` to:
   - Perform **EDA & Feature Engineering**.
   - Train **Multiple Regression Models**.
   - **Tune Hyperparameters** with `GridSearchCV` & `RandomizedSearchCV`.
   - Save the **best model** (`best_rf_model.pkl`) and **scaler** (`scaler.pkl`).

---

## 🚀 **Running the Flask API**
### **1️⃣ Start the Flask App**
```bash
python api/app.py
```
This will start the API server at `http://127.0.0.1:5000/`.

### **2️⃣ Test API with cURL**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
  "bedrooms": 3,
  "bathrooms": 1.5,
  "sqft_living": 1400,
  "sqft_lot": 5000,
  "sqft_above": 1000,
  "sqft_basement": 400
}' http://127.0.0.1:5000/predict
```

### **3️⃣ Test API with Postman**
- Open **Postman**.
- Create a **POST** request to `http://127.0.0.1:5000/predict`.
- Add **JSON body**:
  ```json
  {
    "bedrooms": 3,
    "bathrooms": 2.5,
    "sqft_living": 2200,
    "sqft_lot": 5500,
    "sqft_above": 1700,
    "sqft_basement": 500
  }
  ```
- Click **Send** and receive the **predicted price**!

---

## 🐳 **Docker Setup**
### **1️⃣ Build Docker Image**
```bash
docker build -t house-price-api .
```

### **2️⃣ Run Docker Container**
```bash
docker run -p 5000:5000 house-price-api
```
Now the API is running at `http://127.0.0.1:5000/`.

---
## 🎨 **Simple Frontend (Optional)**
A basic **HTML Form** that interacts with the API:
```html
<form id="predict-form">
    <input type="number" name="bedrooms" placeholder="Bedrooms">
    <input type="number" name="bathrooms" placeholder="Bathrooms">
    <input type="number" name="sqft_living" placeholder="Sqft Living">
    <button type="submit">Predict</button>
</form>
<script>
document.getElementById('predict-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    let data = { bedrooms: 3, bathrooms: 2.5, sqft_living: 2000 };
    let response = await fetch('/predict', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    let result = await response.json();
    alert('Predicted Price: ' + result.predicted_price);
});
</script>
```

---


🚀 **Thank you for checking out this project!** 🚀  
✨ *Happy Coding!* ✨
