
import pandas as pd

INPUT_FILE = "data/raw/sales_dirty.csv"
CLEAN_FILE = "data/cleaned/sales_clean.csv"
REJECTED_FILE = "data/rejected/sales_rejected.csv"

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id",
    "product_id", "quantity", "unit_price", "city"
]


def clean_data():
    df = pd.read_csv(INPUT_FILE)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    original = df.copy()

    # Standardize text.
    for col in ["customer_id", "product_id", "city"]:
        df[col] = df[col].astype("string").str.strip()

    df["city"] = df["city"].str.title()

    # Convert invalid values to missing values.
    for col in ["order_id", "quantity", "unit_price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )

    # Collect all rejection reasons for each row.
    reasons = pd.Series("", index=df.index, dtype="string")

    def reject(mask, message):
        nonlocal reasons
        current = reasons.loc[mask]
        reasons.loc[mask] = current.where(
            current.eq(""), current + "; "
        ) + message

    for col in REQUIRED_COLUMNS:
        reject(df[col].isna(), f"Missing or invalid {col}")

    reject(
        df["order_id"].notna() & (df["order_id"] % 1 != 0),
        "order_id must be an integer"
    )
    reject(
        df["quantity"].notna() & (df["quantity"] % 1 != 0),
        "quantity must be an integer"
    )
    reject(
        df["quantity"].notna() & (df["quantity"] <= 0),
        "quantity must be greater than zero"
    )
    reject(
        df["unit_price"].notna() & (df["unit_price"] <= 0),
        "unit_price must be greater than zero"
    )

    # Reject all rows sharing a duplicate order ID.
    duplicate = (
        df["order_id"].notna()
        & df["order_id"].duplicated(keep=False)
    )
    reject(duplicate, "Duplicate order_id")

    rejected_mask = reasons.ne("")

    rejected = original.loc[rejected_mask].copy()
    rejected["rejection_reason"] = reasons.loc[rejected_mask]

    clean = df.loc[~rejected_mask].copy()

    clean["order_id"] = clean["order_id"].astype("int64")
    clean["quantity"] = clean["quantity"].astype("int64")
    clean["unit_price"] = clean["unit_price"].round(2)
    clean["order_date"] = clean["order_date"].dt.strftime("%Y-%m-%d")

    clean["total_amount"] = (
        clean["quantity"] * clean["unit_price"]
    ).round(2)

    clean.to_csv(CLEAN_FILE, index=False)
    rejected.to_csv(REJECTED_FILE, index=False)

    print(f"Input rows: {len(original)}")
    print(f"Clean rows: {len(clean)}")
    print(f"Rejected rows: {len(rejected)}")

    return clean, rejected


if __name__ == "__main__":
    clean_data()
