# 🚗 Car Price Prediction System

## 📌 Overview

This project is a **full-stack machine learning application** that predicts the price of used cars based on user inputs such as company, model, year, fuel type, and kilometers driven.

It combines a trained ML model with a Flask backend and an interactive frontend to deliver **real-time price predictions**.

---

## 🎯 Features

* 🔍 Real-time car price prediction
* 📊 Machine Learning model (Linear Regression)
* 🌐 Flask-based backend API
* 🎨 Interactive UI with dynamic dropdowns
* ⚡ Fast predictions using AJAX (Fetch API)
* 📁 Clean project structure (templates + static)

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML5
* CSS3
* JavaScript (Fetch API)
* Jinja2 (Templating Engine)
* Pickle (Model Serialization)
* Lucide Icons

---


## 📂 Project Structure

```id="struct1"
CAR_PRICE/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── hero_car.png
│
├── templates/
│   └── index.html
│
├── app.py
├── Cleaned_Car_data.csv
├── LinearRegressionModel.pkl
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```id="cmd1"
git clone https://github.com/your-username/car-price-prediction.git
```

### 2. Navigate to Project

```id="cmd2"
cd car-price-prediction
```

### 3. Create Virtual Environment (Optional)

```id="cmd3"
python -m venv venv
```

### 4. Activate Environment

* Windows:

```id="cmd4"
venv\Scripts\activate
```

* Mac/Linux:

```id="cmd5"
source venv/bin/activate
```

### 5. Install Dependencies

```id="cmd6"
pip install -r requirements.txt
```

### 6. Run Application

```id="cmd7"
python app.py
```

### 7. Open in Browser

```id="cmd8"
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* Model: Linear Regression

* Dataset: Cleaned Car Dataset

* Input Features:

  * Company
  * Model
  * Year
  * Fuel Type
  * Kilometers Driven

* Output:

  * Predicted Car Price (₹)

---

## 🚀 Future Improvements

* Deploy using Streamlit / Flask / Docker
* Add more advanced models (XGBoost, Random Forest)
* Improve UI/UX with animations
* Add user authentication
* Integrate real-time market datasets

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
