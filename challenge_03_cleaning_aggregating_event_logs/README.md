## Objective
Simulate a data engineering task: clean and summarize raw event logs from a mobile app. You'll practice working with nested data, handling missing values, and aggregating results.

## Tasks

- Parse timestamps into Python `datetime` objects.
- Drop events missing `user_id` or `event_type`.
- Compute:
  - Event counts per `event_type`
  - Event counts per `user_id`
  - Daily event totals

## Function Signature

```python
def summarize_events(events: list[dict]) -> dict:
    ...
```

## Function Signature
{
  "user_id": "u1",
  "event_type": "click",
  "timestamp": "2023-01-01T10:01:00",
  "metadata": {"page": "product", "product_id": "p1"}
}

## Expected Output
{
  "event_type_counts": {"view": 2, "click": 2, "purchase": 1},
  "user_event_counts": {"u1": 3, "u2": 2},
  "daily_summary": {"2023-01-01": 3, "2023-01-02": 3}
}