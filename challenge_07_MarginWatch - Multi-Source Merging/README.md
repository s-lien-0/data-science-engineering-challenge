
# Challenge 7 – Multi-Source Merging

This challenge simulates a common data science task in healthcare analytics or health economics: merging transaction-level data with reference product data to perform margin analysis.

---

## 🗂️ Files Included

- `retail_clinical.csv`: Simulated clinical transaction records (e.g., medical supply usage or trial billing).
- `products_clinical.csv`: Product master list with categories and base costs.

---

## 🧪 Objective

Use these datasets to:

1. **Merge** the `retail_clinical.csv` and `products_clinical.csv` on `ProductID`.
2. **Calculate revenue**: `Revenue = Quantity × UnitPrice`
3. **Calculate margin**: `Margin = Revenue - BaseCost × Quantity`
4. **Identify products** with:
   - High sales volume
   - Low or negative margins

---

## 💡 Suggested Questions

- Which product categories are most commonly used across countries?
- Are there any high-usage products that are **low-margin** or **negative-margin**?
- How do margin distributions vary by country?

---

## 🧰 Tools to Practice

- `pandas.merge()`
- Column calculations using vectorized math
- Grouping and filtering (`groupby`, `agg`, `sort_values`)
- Optional: Matplotlib/seaborn visualizations

---

## 🏥 Real-World Analogy

Think of this as merging clinical trial usage logs with procurement data to evaluate the **economic efficiency** of treatment protocols.

