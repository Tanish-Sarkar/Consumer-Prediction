import pandas as pd
import os

# Get the correct file path
current_dir = os.path.dirname(__file__)  # Script's directory
file_path = os.path.join(current_dir, '../data/processed/cleaned_telco.csv')

# Try reading with error handling
try:
    df = pd.read_csv(file_path, encoding='utf-8') 
    
    # Remove spaces in column names
    df.columns = df.columns.str.replace(' ', '')
    # Convert TotalCharges to numeric (handle non-numeric values)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    # Fill missing TotalCharges
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    # First, encode the target column 'Churn'
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    # Identify object columns
    categorical_features = df.select_dtypes(include='object').columns.tolist()

    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']

    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0, 'Male': 1, 'Female': 0})

    df = pd.get_dummies(df, columns=[col for col in categorical_features if col not in binary_cols], drop_first=True)

    # Display them
    # print("Categorical Columns:", categorical_features)
    # print(df.head())
    print(df.head())
    # print(df.info())


    
except Exception as e:
    print(f"Error reading file: {e}")
    print("Trying alternative methods...")
    
    # Try different encodings/delimiters
    try:
        df = pd.read_csv(file_path, encoding='latin1', sep=',', on_bad_lines='skip')
        print("File loaded with latin1 encoding.")
    except Exception as e:
        print(f"Still failing: {e}")
        print("Check if the file exists and is a valid CSV.")