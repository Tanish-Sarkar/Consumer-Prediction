from src.data_loader import load_data
from src.preprocessing import split_data, preprocess_data
from src.model import train_model, evaluate_model, save_model
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
    evaluate_model(model, X_test, y_test)
    save_model(model)

if __name__ == "__main__":
    main()
