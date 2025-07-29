pandas
numpy
matplotlib
seaborn
scikit-learn
joblib



Small snippet to import file in `.py` file with pandas if `pd.read_csv("PATH")`  is not working directly
#
```
import pandas as pd
import os

# Get the correct file path
current_dir = os.path.dirname(__file__)  # Script's directory
file_path = os.path.join(current_dir, '../data/processed/cleaned_telco.csv')

# Try reading with error handling
try:
   
    
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
```