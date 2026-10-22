import pandas as pd
import pytest

from src.validate import validate_data


def valid_data():
    return pd.DataFrame({
        "order_id": [1],
        "order_date": ["2026-10-01"],
        "customer_id": ["C001"],
        "product_id": ["P101"],
        "quantity": [2],
        "unit_price": [500.0],
        "city": ["Indore"],
        "total_amount": [1000.0],
    })


def test_valid_data_passes():
    assert validate_data(valid_data()) is True


def test_duplicate_order_id_fails():
    df = pd.concat(
        [valid_data(), valid_data()],
        ignore_index=True,
    )

    with pytest.raises(ValueError, match="Duplicate"):
        validate_data(df)


def test_zero_quantity_fails():
    df = valid_data()
    df.loc[0, "quantity"] = 0

    with pytest.raises(ValueError, match="quantity"):
        validate_data(df)
