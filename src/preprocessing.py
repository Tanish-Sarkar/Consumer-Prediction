import pandas as pd
import os

# Get the correct file path
current_dir = os.path.dirname(__file__)  # Script's directory
file_path = os.path.join(current_dir, '../data/processed/cleaned_telco.csv')

# Try reading with error handling
try:
    df = pd.read_csv(file_path, encoding='utf-8')  # Try 'latin1' if UTF-8 fails
    print("File loaded successfully!")
    print(df.head())
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