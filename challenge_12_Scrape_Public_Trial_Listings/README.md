# Clinical Trial Scraper – Type 2 Diabetes (Challenge 12)

This project extracts structured data from clinicaltrials.gov for recent **interventional studies** related to **Type 2 Diabetes**.

---

## 🎯 Goal

Scrape the **latest 100 interventional trials** for **"Type 2 Diabetes"**, normalize the information, and export a clean `.csv` with useful metadata for downstream analysis.

---

## 🔍 Data Source

- Target: [ClinicalTrials.gov](https://clinicaltrials.gov/)
- URL template:  
  https://clinicaltrials.gov/ct2/results?cond=Type+2+Diabetes&type=Intr&sort=dat
- Data pulled dynamically via `requests` and parsed with `BeautifulSoup`.

---

## 📦 Output

**File:** `output/trials_diabetes.csv`  
**Columns:**

| Column       | Description                                        |
|--------------|----------------------------------------------------|
| `title`      | Title of the clinical study                        |
| `condition`  | Disease or condition studied (must include T2D)    |
| `intervention` | Drug or therapy being tested (normalized)       |
| `location`   | Trial location (city/state or country)             |

---

## 🚀 How to Run

```bash
python scrape_trials.py
