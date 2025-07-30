# 💊 Challenge 15 – Dynamic Drug Pricing Optimization

## 👩‍⚕️ Client: ApexCare Pharma Logistics

### 📘 Context
ApexCare is a pharmaceutical distributor serving hundreds of hospitals and pharmacies. Each drug has a **target inventory level** (base stock), but actual stock levels fluctuate daily due to demand, delivery delays, and overstocking.

ApexCare’s pricing team wants to **automate price adjustments** daily to reflect supply changes across locations. You're brought in to prototype this dynamic pricing logic.

---

## 🧠 Business Goal

Implement a **pricing algorithm** that:
- **Increases prices** for understocked items
- **Decreases prices** for overstocked items
- Keeps prices stable when supply is on target
- Reflects **stronger changes** when deviation is higher

---

## 📊 Dataset Description

Each row is a **drug-location record**, representing a stock snapshot for that drug at a particular hospital or pharmacy.

> Note: Each row is independent. You are **not guaranteed** that every drug has the same base stock everywhere.

| Column         | Description                                                  |
|----------------|--------------------------------------------------------------|
| `item`         | Name of the drug (e.g., Metformin)                           |
| `base_stock`   | Target inventory level for this item at this location        |
| `current_stock`| Current inventory level                                      |
| `price`        | Current price (float)                                        |

---

## 📌 Pricing Rules

Your function should calculate a new price for each row based on:

- If `current_stock == base_stock`:
  ```python
  adjusted_price = price
  ```

- If `current_stock < base_stock`:
  ```python
  rate_increase = min(0.5, 0.02 * (base_stock - current_stock))
  adjusted_price = price * (1 + rate_increase)
  ```

- If `current_stock > base_stock`:
  ```python
  rate_decrease = min(0.3, 0.015 * (current_stock - base_stock))
  adjusted_price = price * (1 - rate_decrease)
  ```

Final prices should be rounded to 2 decimals.

---

## ✅ Your Task

Write a function:

```python
def adjust_prices(df: pd.DataFrame) -> pd.DataFrame:
```

**Requirements:**
- Add a new column `'adjusted_price'`
- Preserve all original columns
- Use vectorized pandas logic (no loops)

---

## 🧪 Evaluation Criteria

| Area         | Metric                                 |
|--------------|-----------------------------------------|
| 🧠 Logic      | Follows pricing rules precisely         |
| ⚡️ Efficiency | Vectorized, performant code             |
| 🔁 Reusability| Clean function, no hardcoded assumptions|
| ✅ Realism    | Handles edge cases (e.g., 0 stock)      |

---

## 🚀 Bonus

Add logic to:
- Flag large increases/decreases (e.g., >20%) in a new column
- Visualize average price change per drug

---

## 📂 Files
- `mock_drug_inventory.csv` (optional generated data)
- `analysis.ipynb` (your function)
- `README.md` (this file)

---

Take on the role of an internal **data science consultant** helping ApexCare optimize their pricing strategy using data!
