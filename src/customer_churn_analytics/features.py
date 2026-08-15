import pandas as pd
from pathlib import Path

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates new features based on the cleaned dataset.
    """
    df = df.copy()
    
    df["is_monthly_contract"] = (df["Contract Length"] == "Monthly").astype(int)
    df["high_support_calls"] = (df["Support Calls"] >= 6).astype(int)
    
    bins = [-1, 2, 5, 8, 10]
    labels = ["Low", "Medium", "High", "Very high"]
    df["support_calls_bucket"] = pd.Categorical(
        pd.cut(df["Support Calls"], bins=bins, labels=labels), 
        categories=labels, 
        ordered=True
    )
    
    df["low_spend_customer"] = (df["Total Spend"] < 500).astype(int)
    df["payment_delay_over_18"] = (df["Payment Delay"] > 18).astype(int)
    df["disengaged"] = (df["Last Interaction"] > 14).astype(int)
    
    risk_flags = [
        "is_monthly_contract",
        "high_support_calls",
        "low_spend_customer",
        "payment_delay_over_18",
        "disengaged",
    ]
    df["risk_score"] = df[risk_flags].sum(axis=1)
    
    return df

if __name__ == "__main__":
    PROCESSED_DIR = Path("data/processed")
    
    train = pd.read_csv(PROCESSED_DIR / "train_clean.csv")
    test = pd.read_csv(PROCESSED_DIR / "test_clean.csv")
    
    train_features = engineer_features(train)
    test_features = engineer_features(test)
    
    train_features.to_csv(PROCESSED_DIR / "train_features.csv", index=False)
    test_features.to_csv(PROCESSED_DIR / "test_features.csv", index=False)
    print("Feature engineering completed.")
