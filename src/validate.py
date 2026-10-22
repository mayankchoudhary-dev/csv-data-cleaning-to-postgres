
import pandas as pd

CLEAN_FILE = "data/cleaned/sales_clean.csv"

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id", "product_id",
    "quantity", "unit_price", "city", "total_amount"
]


def validate_data(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError("Null values found")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found")

    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid quantity found")

    if (df["unit_price"] <= 0).any():
        raise ValueError("Invalid unit price found")

    expected = (df["quantity"] * df["unit_price"]).round(2)

    if not expected.equals(df["total_amount"].round(2)):
        raise ValueError("Incorrect total_amount calculation")

    print("All data quality checks passed.")
    return True


if __name__ == "__main__":
    df = pd.read_csv(CLEAN_FILE)
    validate_data(df)
