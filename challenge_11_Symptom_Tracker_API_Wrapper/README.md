# Challenge 11 – Symptom Tracker API Wrapper

## Overview

You're building a reusable client for a symptom tracking API. The API returns JSON entries that include:
- `date`
- `symptoms` (list)
- `severity` (int)
- `notes` (optional)

## Your Task
- Create a `SymptomEntry` class.
- Build a `SymptomTrackerClient` that:
  - Loads data from the JSON source
  - Converts to SymptomEntry objects
  - Supports `.get_by_date()`, `.filter_by_severity()`
  - Outputs `.to_dataframe()`
  - Adds helpful properties (e.g., `entry_count`, `latest_entry`)

Use the provided `mock_api.json` to simulate API data.

## 🧪 Example Usage

```python
from client import SymptomTrackerClient

tracker = SymptomTrackerClient()
print(tracker.entry_count)

df = tracker.to_dataframe()
filtered = tracker.filter_by_severity(3)
