from src.data_loader import load_data
from src.preprocessing import preprocess_data, split_data
from src.model import train_model, save_model
from src.evaluation import evaluate_model, plot_confusion_matrix
from src.utils import save_metrics
import os

def main():
    current_dir = os.path.dirname(__file__)  
    file_path = os.path.join(current_dir, './data/processed/Cleaned_Telco.csv')

    df = load_data(file_path)
    print("✅ Data Loaded Successfully...")
    print(f"Shape: {df.shape}")

    X, y = preprocess_data(df)
    print("✅ Data Preprocessed...")

    X_train, X_test, y_train, y_test = split_data(X, y)
    print("✅ Data Split into Train/Test")

    model = train_model(X_train, y_train)
    print("✅ Model Trained...")

    metrics = evaluate_model(model, X_test, y_test)
    print("✅ Model Evaluated...")

    print("📊 Plotting Confusion Matrix...")
    y_pred = model.predict(X_test)
    plot_confusion_matrix(y_test, y_pred)

    print("💾 Saving Model and Metrics...")
    save_model(model, "outputs/LogisticModel.joblib")
    save_metrics(metrics)

if __name__ == "__main__":
    main()
