import pandas as pd

def clean_order_df(df: pd.DataFrame) -> pd.DataFrame:
    """Clean order data: fix types, calculate derived fields, and flag repeat customers."""
    df = df.copy()

    if df is None:
        return pd.DataFrame()

    # Convert timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Defensive checks
    if "quantity" not in df or "product_unit_price" not in df:
        raise ValueError("Missing columns for revenue calculation.")

    # Derived field: total value of order
    df["order_value"] = df["quantity"] * df["product_unit_price"]

    # Flag repeat customers
    df["is_repeat_customer"] = df["customer_id"].duplicated(keep=False)

    return df