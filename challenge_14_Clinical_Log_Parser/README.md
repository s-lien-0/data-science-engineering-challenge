# 🩺 Clinical Log Parser – Challenge 14

Convert messy, semi-structured nurse logs into clean, structured data using regex and Python.

---

## 🧾 Example Input (Raw Log)

```text
Patient: Jane Doe | Temp: 38.5°C | BP: 130/85 | Notes: Mild cough  
Patient: Alex R. | Temp: -- | BP: not taken | Notes: "complained of fatigue"
```

---

## ✅ Output Formats

### JSON
```json
[
  {
    "patient_name": "Jane Doe",
    "temperature": 38.5,
    "bp_systolic": 130,
    "bp_diastolic": 85,
    "notes": "Mild cough"
  },
  {
    "patient_name": "Alex R.",
    "temperature": null,
    "bp_systolic": null,
    "bp_diastolic": null,
    "notes": "complained of fatigue"
  }
]
```

### CSV (example)

| patient_name | temperature | bp_systolic | bp_diastolic | notes                 |
|--------------|-------------|-------------|--------------|------------------------|
| Jane Doe     | 38.5        | 130         | 85           | Mild cough             |
| Alex R.      |             |             |              | complained of fatigue  |

---

## 🧠 What This Script Does

- Uses regex patterns to extract fields:  
  - `patient_name`, `temperature`, `bp_systolic`, `bp_diastolic`, `notes`
- Handles dirty or missing values gracefully:
  - Recognizes placeholders like `--`, `not taken`, empty quotes
  - Converts to `null` (or `None` in Python)
- Converts logs to:
  - JSON
  - CSV
- Can be easily extended to support CLI, validation, or analysis

---

## 🚀 How to Run

```bash
python clinical_log_parser.py --input logs.txt --output parsed.json
```

### Optional CLI Flags
- `--format json|csv` (default: `json`)
- `--validate` – Apply extra checks (e.g., temp must be a float)
- `--summary` – Print quick stats (e.g., % missing temps)

---

## 🧪 Testing

Basic unit tests are included in `test_parser.py` using `pytest`.

```bash
pytest test_parser.py
```

---

## 🧩 Design Notes

- **Regex-first parsing** avoids over-relying on string splits.
- **Modular functions**: `parse_log_line`, `parse_all_logs`, `export_to_json`, `export_to_csv`
- **Validation** (optional): Can be added with `pydantic` or manual checks

---

## 📈 Bonus Features (Optional)

- Summary report of missing fields and distribution of vitals
- Extend to CLI tool with `argparse`
- Integrate into broader data ingestion pipeline
