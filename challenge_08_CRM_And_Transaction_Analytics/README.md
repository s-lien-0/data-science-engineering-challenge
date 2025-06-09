# 🧬 Challenge 8: Nested JSON Flattening & Transaction Enrichment

## 📦 Project Overview

This project simulates a real-world task of converting **nested JSON order data** into a clean, flat DataFrame suitable for analytics. The goal is to extract and normalize transaction, customer, and product data — as often done in CRM and business intelligence pipelines.

---

## 📁 Dataset Description

- `orders_nested.json`: A mock dataset containing 3 order records.
  - Each order contains:
    - `order_id`, `timestamp`
    - `customer` (id, name, email)
    - `product` (id, name, category, unit price)
    - `quantity`
    - `shipping` (method, cost)

---

## ✅ Objectives

1. **Load JSON Data**  
   Safely load nested JSON using defensive file handling.

2. **Flatten Nested Records**  
   Use `pandas.json_normalize()` to convert embedded structures into tabular columns.

3. **Standardize & Clean Columns**
   - Convert `timestamp` to datetime
   - Rename to `snake_case`
   - Compute derived fields like `order_value = unit_price × quantity`

4. **Customer Enrichment**  
   - Flag `is_repeat_customer` based on `customer_id` occurrence.

---

## 📊 Output

- A flat, analysis-ready DataFrame with one row per order.
- Cleaned columns such as:
  - `order_id`, `customer_id`, `product_name`, `order_value`, `is_repeat_customer`, etc.
- Optional:
  - CSV export (`flattened_orders.csv`)
  - Summary stats (`top customers`, `top products`, etc.)

---

## 🛠️ Core Functions

```python
def load_json_file(filepath: str) -> dict
def flatten_orders(data: dict) -> pd.DataFrame
def clean_order_df(df: pd.DataFrame) -> pd.DataFrame
def enrich_with_history(df: pd.DataFrame, history: pd.DataFrame) -> pd.DataFrame