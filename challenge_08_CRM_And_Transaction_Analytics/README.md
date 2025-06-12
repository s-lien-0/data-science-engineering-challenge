# 🧪 Nested Order JSON Pipeline

This CLI data pipeline loads nested JSON order records, flattens and cleans the data, joins it with historical product info, and outputs summary reports.

---

## 📦 Features

- ✅ Loads nested JSON (orders)
- ✅ Flattens `customer`, `product`, and `shipping` fields
- ✅ Cleans & derives fields (`timestamp`, `order_value`, `is_repeat_customer`)
- ✅ Joins with `product_history.csv` to calculate margin
- ✅ Outputs:
  - Console summary
  - Bar plot: `reports/top_products_margin.png`
  - Enriched CSV: `reports/enriched_orders.csv`

---

## 🚀 How to Run

Make sure you have Python 3.10+ and install dependencies:

```bash
pip install pandas matplotlib seaborn pytest