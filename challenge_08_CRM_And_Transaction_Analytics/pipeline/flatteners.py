import pandas as pd
from pandas import json_normalize

def flatten_orders(data: list[dict]) -> pd.DataFrame:
    """Flatten nested fields (customer, product, shipping) from order records."""
    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    customer_df = json_normalize(df["customer"]).add_prefix("customer_")
    product_df = json_normalize(df["product"]).add_prefix("product_")
    shipping_df = json_normalize(df["shipping"]).add_prefix("shipping_")

    flat_df = pd.concat([
        df.drop(columns=["customer", "product", "shipping"]),
        customer_df,
        product_df,
        shipping_df
    ], axis=1)

    return flat_df