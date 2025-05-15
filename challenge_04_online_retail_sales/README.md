# 🧪 Challenge 4 – Modular Data Cleaning & Aggregation

## 🎯 Objective

Refactor your data cleaning and analysis code into clean, reusable **functions** with proper **error handling** and **edge-case management**.

This simulates working with real-world retail transaction data where code quality, maintainability, and clarity matter.

---

## 📊 Dataset

A sample of the **Online Retail Dataset** (CSV format), with fields like:

- `InvoiceNo` — Transaction ID
- `StockCode` — Product code
- `Description` — Product name
- `Quantity` — Units purchased (may include returns)
- `InvoiceDate` — Date and time of transaction
- `UnitPrice` — Price per item
- `CustomerID` — Customer identifier (can be missing)
- `Country` — Country of customer

---

## 🛠️ Tasks

1. **Load the dataset**
   - Use a function: `load_data(filepath)`
   - Add error handling for file not found or read errors

2. **Clean the dataset**
   - Write a function: `clean_data(df)`
   - Handle missing `CustomerID`, remove negative/zero quantities
   - Ensure correct data types (`InvoiceDate`, `UnitPrice`, etc.)

3. **Aggregate sales**
   - Create function(s) to calculate:
     - Revenue by `Country`
     - Revenue by `StockCode` or `Description`
   - Use `Quantity * UnitPrice` to compute revenue

4. **Filter by date range**
   - Optional function: `filter_data_by_date(df, start_date, end_date)`

5. **Save cleaned output**
   - Use `save_clean_data(df, output_path)` to export cleaned results

---

## ✅ Deliverables

- A Python script or Jupyter notebook with:
  - Modularized functions
  - Proper error handling (`try/except`)
  - Comments/docstrings explaining function purpose

- Cleaned CSV output file

- (Optional) Git commits showing before/after refactor if you're tracking progress

---

## 💡 Bonus Ideas

- Add logging or print statements for clarity
- Add type hints to your functions
- Handle possible malformed rows, duplicates, or missing descriptions

---

## 🔍 Example Analysis Questions

- Which country generated the most revenue?
- Which products are the top sellers by quantity or revenue?
- Are there patterns in returns (negative quantities)?

---
