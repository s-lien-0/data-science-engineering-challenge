# 🗓️ Sales Lag Tracker

A lightweight Python utility for computing the **number of days between consecutive orders per customer**.  
Built for analysts and data engineers who want **reusable, vectorized lag calculations** without manual date diffs.

## 💼 Business Use Cases
The Sales Lag Tracker isn't just a technical tool — it solves a business problem: **understanding customer buying behavior**.

### 1. Customer Retention Tracking
- Measure how long customers wait before coming back.
- Identify customers whose purchase frequency is dropping — potential churn risks.
- Spot loyal customers with consistently short lag times.

### 2. Targeted Marketing & Promotions
- Trigger automated emails or app notifications when a customer's lag exceeds their normal pattern.
- Offer time-sensitive discounts to bring customers back sooner.

### 3. Inventory & Demand Forecasting
- Anticipate when repeat orders are likely to occur.
- Plan stock levels more accurately to reduce overstock or stockouts.

### 4. Customer Segmentation
- Group customers into "frequent buyers" vs. "occasional buyers".
- Compare lag patterns across different regions, product categories, or demographics.

### 5. Campaign Performance Measurement
- Check if marketing efforts successfully shorten customer lag times.
- Measure seasonal or event-based changes in buying behavior.

> **Example:**  
> If the average coffee shop customer buys every 5 days, but your loyalty campaign brings that down to 3 days, you’ve just increased revenue and engagement.

---

## 📌 Overview

**Problem:**  
Client needs to track repeat customer behavior and measure the gap between purchases.

**Solution:**  
A reusable function `sales_lag_tracker(df, customer_col, date_col)` that:
- Sorts by customer and date
- Calculates the difference (in days) between each order and the previous one
- Handles **edge cases** (first order = `NaN` lag)

---

## 🚀 Features
- **Reusable** – works on any DataFrame with customer/date columns
- **Vectorized** – uses `groupby` + `shift` for fast execution
- **Defensive** – validates input columns and handles missing/invalid dates
- **Flexible** – accepts any customer ID and date column names