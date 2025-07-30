import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=3000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}\n")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}\n")
    print(f"Classification Report:\n{classification_report(y_test, y_pred)}\n")

def save_model(model, path='outputs/LogisticModel.joblib'):
    # Ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save the model
    joblib.dump(model, path)
    print(path)
    print("✅ Model saved to 'outputs' directory.")
