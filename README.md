# FunQi - Function Quality Intelligence

FunQi (Function Quality Intelligence) is a **machine learning-powered platform** that evaluates Python functions based on multiple code quality metrics. It provides **automated code quality scores** and **improvement suggestions**, making it useful for developers, software teams, and educators.

## 🚀 Features
- 📊 **Code Quality Analysis**: Extracts features like **cyclomatic complexity, modularity, function naming, comment quality, and more** from function.
- 🤖 **Machine Learning-Powered**: Uses **trained ML models** (Random Forest) for accurate predictions of code quality score.
- 🔍 **Detailed Feedback**: Provides suggestions to improve **code readability, maintainability, and efficiency**.
  
---

## 🏗️ Architecture & Approach
### 1️⃣ Problem Identification & Goal
Current platforms focus on rule-based analysis or syntax correctness. FunQi aims to **predict code quality dynamically** using machine learning.

### 2️⃣ Dataset Creation
- Built a dataset with **six key parameters**: Cyclomatic Complexity, Loops, Function Length, Modularity, Comment Quality, and Naming Quality.
- Assigned an **ideal quality score** based on these parameters for supervised learning.

### 3️⃣ Preprocessing & Model Training
- Used **MinMaxScaler** for normalization.
- Correlation analysis to validate meaningful features.
- Trained multiple ML models (Random Forest, SVM, Gradient Boosting, KNN) and selected the best performers.

### 4️⃣ Algorithm for Metric Calculations
- Extracts **AST-based** metrics using **Radon** and **custom Python functions**.
- **NLP techniques** (NLTK) for analyzing **comment quality** and **function names**.

### 5️⃣ Web App & API Development
- **Backend**: Flask API for model inference.
- **Frontend**: HTML, CSS, JavaScript for UI.
- **Testing**: Verified API responses using **Postman**.

---
## ML Model Results

---

## 🛠️ Technologies Used
- **Python, Flask** (Backend)
- **scikit-learn, NLTK, Radon, Numpy, Pandas** (ML & Code Analysis)
- **HTML, CSS, JavaScript** (Frontend)
- **Postman** (API Testing)
---

## 📥 Installation & Usage
### 🔧 Prerequisites
- Python 3.x
- Flask
- scikit-learn, NLTK, Radon

### 🔹 Clone the Repository
```sh
$ git clone https://github.com/yourusername/FunQi.git
$ cd FunQi
```

### 🔹 Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 🔹 Run the Flask App
```sh
$ python app.py
```

### 🔹 API Usage
Send a **POST request** with a Python function to analyze:
```sh
$ curl -X POST "http://localhost:5000/analyze" -H "Content-Type: application/json" -d '{"code": "def example():\n    print(\"Hello, World!\")"}'
```

---

