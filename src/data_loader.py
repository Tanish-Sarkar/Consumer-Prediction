import pandas as pd

def load_data(path: str):
    try:
        df = pd.read_csv(path, encoding='utf-8') 
        return df   
    
    except Exception as e:
        print(f"Error reading file: {e}")
        print("Trying alternative methods...")

        try:
            df = pd.read_csv(path, encoding='latin1')
            print("File loaded with latin1 encoding.")
            return df
        except Exception as e:
            print(f"Still failing: {e}")
            raise FileNotFoundError("Check if the file exists and is a valid CSV.")
