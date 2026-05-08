import pandas as pd
from pipeline.sales_transform import clean_sales_data


def test_clean_sales_data_removes_null_customer():
    data = {
        "customer_id": [1, None],
        "sales_amount": [100, 200]
    }

    df = pd.DataFrame(data)

    result = clean_sales_data(df)

    assert len(result) == 1
    assert result.iloc[0]["customer_id"] == 1


def test_clean_sales_data_fills_null_sales():
    data = {
        "customer_id": [1, 2],
        "sales_amount": [100, None]
    }

    df = pd.DataFrame(data)

    result = clean_sales_data(df)

    assert result.iloc[1]["sales_amount"] == 0
