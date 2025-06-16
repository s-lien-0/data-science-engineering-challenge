## Client Request: Data Validation Layer for Product, Order, and Customer Files

### Project Background

Our analytics and reporting pipelines depend on daily uploads of product, order, and customer data. Recently, we have experienced broken dashboards and failed batch jobs caused by invalid or incomplete data files. We want to avoid any bad data from entering our pipeline by adding robust, automated validation.

---

### Request

**Objective:**  
Please implement a data validation layer for our pipeline, covering all major incoming files (products, customers, orders, and config). The validator should:

- **Check for required fields and correct data types** in each file.
- **Catch common errors**, such as missing values, empty strings, negative prices, or invalid email formats.
- **Provide clear, actionable error messages** indicating the exact problem and location (row/index and field name).
- **Support batch validation:** If multiple issues exist, report all at once—so we can fix everything in a single pass.
- **Include automated tests** for your validators, covering both “good” (valid) and “bad” (invalid/malformed) data scenarios.
- **(Bonus)**: Use Pydantic for concise schema enforcement and better error reporting.

---

### Validation Rules

#### **Product File**
- `product_id` must be present and not empty.
- `name` must be present and not empty.
- `price` must be a number (int or float) and not negative.

#### **Customer File**
- `customer_id` must be present and not empty.
- `name` must be present and not empty.
- `email` (if present) must be a valid email address.

#### **Order File**
- `order_id` and `customer_id` must be present and not empty.
- `items` must be a non-empty list.
- `date` must be a valid date string.

#### **Config File**
- Required settings must be present, with correct types.

---

### Success Criteria

- If a file is invalid, the pipeline halts and returns a clear error report.
- If all files pass validation, pipeline continues.
- All code is tested and reproducible.

---

**Please reach out if you need sample files, or want to clarify edge cases!**

---

*Retail Insights Analytics — Data Engineering Team*