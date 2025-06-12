import pytest
import pandas as pd
from pipeline.data_loaders import load_json_file
from pipeline.flatteners import flatten_orders
from pipeline.cleaners import clean_order_df
from pipeline.enrichers import enrich_with_history

# ---- load_json_file ----

def test_load_json_valid(tmp_path):
    path = tmp_path / "sample.json"
    path.write_text('[{"order_id": "1", "customer": {}, "product": {}, "shipping": {}, "quantity": 1, "product_unit_price": 1.0, "timestamp": "2025-01-01"}]')
    result = load_json_file(str(path))
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

def test_load_json_invalid_type():
    result = load_json_file(123)
    assert result is None

# ---- flatten_orders ----

def test_flatten_orders_creates_prefixed_columns():
    data = [{
        "order_id": "1",
        "customer": {"id": "C1"},
        "product": {"id": "P1"},
        "shipping": {"cost": 5},
        "quantity": 2,
        "product_unit_price": 10.0,
        "timestamp": "2025-01-01"
    }]
    df = flatten_orders(data)
    assert "customer_id" in df.columns
    assert "product_id" in df.columns
    assert "shipping_cost" in df.columns

# ---- clean_order_df ----

def test_clean_order_df_adds_order_value_and_repeat_flag():
    df = pd.DataFrame([
        {"customer_id": "A", "timestamp": "2025-01-01", "quantity": 2, "product_unit_price": 5.0},
        {"customer_id": "A", "timestamp": "2025-01-02", "quantity": 1, "product_unit_price": 5.0}
    ])
    result = clean_order_df(df)
    assert "order_value" in result.columns
    assert result["order_value"].tolist() == [10.0, 5.0]
    assert result["is_repeat_customer"].all()

# ---- enrich_with_history ----

def test_enrich_with_history_calculates_margin():
    orders = pd.DataFrame([
        {"product_id": "P1", "order_value": 20.0, "quantity": 2}
    ])
    history = pd.DataFrame([
        {"product_id": "P1", "base_cost": 5.0}
    ])
    enriched = enrich_with_history(orders, history)
    assert "margin" in enriched.columns
    assert enriched["margin"].iloc[0] == 10.0

# ---- generate_summary ----

from pipeline.reporting import generate_summary

def test_generate_summary_runs(capfd):
    df = pd.DataFrame([
        {"product_name": "A", "customer_id": "X", "margin": 10.0, "order_value": 50, "is_repeat_customer": True}
    ])
    generate_summary(df)
    out, _ = capfd.readouterr()
    assert "Top Products" in out or "Repeat Customer" in out
