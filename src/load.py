
import pandas as pd
import psycopg

from config.config import DB_CONFIG

INPUT_FILE = "data/cleaned/sales_clean.csv"


def load_data():
    df = pd.read_csv(INPUT_FILE)

    records = [
        (
            int(row.order_id),
            row.order_date,
            row.customer_id,
            row.product_id,
            int(row.quantity),
            float(row.unit_price),
            row.city,
            float(row.total_amount),
        )
        for row in df.itertuples(index=False)
    ]

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO cleaned_sales (
                    order_id, order_date, customer_id, product_id,
                    quantity, unit_price, city, total_amount
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id) DO UPDATE SET
                    order_date = EXCLUDED.order_date,
                    customer_id = EXCLUDED.customer_id,
                    product_id = EXCLUDED.product_id,
                    quantity = EXCLUDED.quantity,
                    unit_price = EXCLUDED.unit_price,
                    city = EXCLUDED.city,
                    total_amount = EXCLUDED.total_amount;
                """,
                records,
            )

    print(f"Successfully loaded {len(records)} records.")


if __name__ == "__main__":
    load_data()
