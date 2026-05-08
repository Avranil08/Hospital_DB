def clean_sales_data(df):
    df = df.dropna(subset=["customer_id"])
    df["sales_amount"] = df["sales_amount"].fillna(0)
    return df
