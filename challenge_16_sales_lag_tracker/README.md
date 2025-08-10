# 🗓️ Sales Lag Tracker

Compute **days between consecutive orders per customer** and operationalize that signal to **trigger timely retention messages**.  
Designed for analysts and data engineers who need a **reusable, vectorized** component that integrates cleanly into marketing and CRM workflows.

---

## Purpose & Outcomes

- **Retention monitoring:** quantify customer purchase frequency and detect overdue return cycles.
- **Targeted outreach:** generate an **eligible audience** for re-engagement when a customer is late versus their norm.
- **Operational planning:** use lag distributions for light demand planning and stock decisions.

### Notification Rules (default)
Use per-customer behavior to avoid blanket messaging:
- **Baseline:** `median_lag` = median of `days_since_last_order`; `recency_days` = days since last order.
- **Eligibility:**  
  - `order_count ≥ 2` (requires history)  
  - `recency_days ≥ 30` (cool-off; avoid premature nudges)  
  - `recency_days > 1.5 × median_lag` (meaningfully overdue)
- **Safeguards:** channel preferences, opt-outs, cool-off (≥14 days since last message), quarterly cap (≤3).

_These thresholds are configurable; start conservative, A/B test, then tune._

**Reference (pandas):**
```python
summary['should_notify'] = (
    (summary['order_count'] >= 2) &
    summary['median_lag'].notna() &
    (summary['recency_days'] >= 30) &
    (summary['recency_days'] > 1.5 * summary['median_lag'])
)