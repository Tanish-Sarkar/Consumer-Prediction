import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)

    service_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'MultipleLines']
    for col in service_cols:
        df[col] = df[col].replace({'No internet service': 'No', 'No phone service': 'No'})

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

    # Only map if not already numeric
    if df['Churn'].dtype == 'object':
        print("Unique values in 'Churn' before encoding:", df['Churn'].unique())
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Label encode + scale
    cat_cols = X.select_dtypes(include='object').columns
    le = LabelEncoder()
    scaler = StandardScaler()
    for col in cat_cols:
        X[col] = le.fit_transform(X[col])
        X[col] = scaler.fit_transform(X[[col]])
  
    print(f"✅ Missing values in y: {y.isnull().sum()}")
    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)
