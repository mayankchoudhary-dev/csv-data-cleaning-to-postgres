import pandas as pd

INPUT_FILE = "data/raw/sales_dirty.csv"


def inspect_data():
    df = pd.read_csv(INPUT_FILE)

    print("\n--- First 5 rows ---")
    print(df.head())

    print("\n--- Dataset dimensions ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n--- Data types ---")
    print(df.dtypes)

    print("\n--- Missing values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate order IDs ---")
    print(df[df.duplicated("order_id", keep=False)])

    print("\n--- Dataset information ---")
    df.info()


if __name__ == "__main__":
    inspect_data()