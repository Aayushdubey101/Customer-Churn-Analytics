import pandas as pd
from pathlib import Path

def load_and_clean_data(raw_dir: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads train and test datasets from the raw directory, cleans them by removing
    duplicates and null values, and returns the cleaned DataFrames.
    """
    raw_dir = Path(raw_dir)
    
    train = pd.read_csv(raw_dir / "train.csv")
    test = pd.read_csv(raw_dir / "test.csv")
    
    # Remove duplicates based on CustomerID and drop nulls
    train_clean = train.drop_duplicates(subset="CustomerID").dropna()
    test_clean = test.drop_duplicates(subset="CustomerID").dropna()
    
    return train_clean, test_clean

if __name__ == "__main__":
    RAW_DIR = Path("data/raw")
    PROCESSED_DIR = Path("data/processed")
    
    train_clean, test_clean = load_and_clean_data(RAW_DIR)
    
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    train_clean.to_csv(PROCESSED_DIR / "train_clean.csv", index=False)
    test_clean.to_csv(PROCESSED_DIR / "test_clean.csv", index=False)
    print("Data cleaning completed.")
