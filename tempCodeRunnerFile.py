
        print(f"Error reading file: {e}")
        print("Trying alternative methods...")
        
        # Try different encodings/delimiters
        try:
            df = pd.read_csv(file_path, encoding='latin1', sep=',', on_bad_lines='skip')
            print("File loaded with latin1 encoding.")
            return df
        except Exception as e:
            print(f"Still failing: {e}")
            print("Check if the file exists and is a valid CSV.")
    

    print("Data Loaded Sucessfully...")
    print(f"Shape: {df.shape}")
    print(df.head())
     

if __name__ == "__main__":
    main()
