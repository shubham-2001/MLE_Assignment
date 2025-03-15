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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>House Price Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 50px auto;
            text-align: center;
        }
        input, button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        #result {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
            color: #007bff;
        }
    </style>
</head>
<body>

    <h2>🏡 House Price Prediction</h2>
    
    <form id="predict-form">
        <input type="number" name="bedrooms" placeholder="Bedrooms" required>
        <input type="number" name="bathrooms" placeholder="Bathrooms" step="0.5" required>
        <input type="number" name="sqft_living" placeholder="Sqft Living" required>
        <input type="number" name="sqft_lot" placeholder="Sqft Lot" required>
        <input type="number" name="sqft_above" placeholder="Sqft Above" required>
        <input type="number" name="sqft_basement" placeholder="Sqft Basement" required>
        <button type="submit">Predict</button>
    </form>

    <div id="result"></div>

    <script>
    document.getElementById('predict-form').addEventListener('submit', async function(event) {
        event.preventDefault();

        let formData = new FormData(event.target);
        let data = {
            bedrooms: parseFloat(formData.get("bedrooms")),
            bathrooms: parseFloat(formData.get("bathrooms")),
            sqft_living: parseFloat(formData.get("sqft_living")),
            sqft_lot: parseFloat(formData.get("sqft_lot")),
            sqft_above: parseFloat(formData.get("sqft_above")),
            sqft_basement: parseFloat(formData.get("sqft_basement"))
        };

        try {
            let response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            let result = await response.json();
            if (response.ok) {
                document.getElementById("result").innerText = "Predicted Price: $" + result.predicted_price.toLocaleString();
            } else {
                document.getElementById("result").innerText = "Error: " + (result.error || "Something went wrong.");
            }

        } catch (error) {
            document.getElementById("result").innerText = "Error: Failed to connect to the server.";
        }
    });
    </script>

</body>
</html>
```

---


🚀 **Thank you for checking out this project!** 🚀  
✨ *Happy Coding!* ✨
