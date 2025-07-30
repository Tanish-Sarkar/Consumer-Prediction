
```markdown
#  Customer Churn Prediction

A complete Machine Learning pipeline built using Scikit-learn for predicting customer churn in a telecom company. The project is modular, production-ready, and follows a structured folder architecture for clarity and reusability.

---

## 🔧 Features

- End-to-end ML pipeline (EDA → Preprocessing → Modeling → Evaluation)
- Clean and scalable project structure
- Model saving with `joblib`
- Performance metrics saved in JSON
- Confusion matrix visualization
- Ready to plug into Flask/Streamlit for deployment

---
````
## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

---

## 📈 Dataset

Telco Customer Churn dataset from Kaggle:
[Telco Churn on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🧠 Algorithms Used

* Logistic Regression (baseline)
* Preprocessing: Label Encoding, StandardScaler
* Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

---

## 🗃 Outputs

* ✅ Model file: `outputs/LinearModel.joblib`
* ✅ Metrics: `outputs/metrics.json`
* ✅ Confusion Matrix: `matplotlib` plot displayed on evaluation

---

## ✍️ Author

* **Tanish Sarkar**
* LinkedIN: [Tanish Sarkar](https://www.linkedin.com/in/tanish-sarkar/)
* Twitter/X: [Tanish Sarkar](https://twitter.com/)

---

## 📌 Future Work

* Add advanced models (RandomForest, XGBoost)
* Deploy using Flask or Streamlit
* Add CI/CD and Docker
* Extend for A/B testing and monitoring (MLOps)

---

## ⭐️ If you found this project helpful


