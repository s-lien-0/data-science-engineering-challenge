import pandas as pd

def enrich_with_history(df: pd.DataFrame, history: pd.DataFrame) -> pd.DataFrame:
    """Join product cost history and compute margin."""
    df = df.copy()
    df = df.merge(history, how='left', on='product_id')

    if 'base_cost' not in df:
        raise ValueError("Missing 'base_cost' in history data.")

    df['margin'] = df['order_value'] - (df['quantity'] * df['base_cost'])
    df['margin'] = df['margin'].round(2)

    return df
