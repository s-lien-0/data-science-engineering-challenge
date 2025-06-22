# 🏥 Hospital Visit Analytics – Config-Driven Pipeline

### 📦 Deliverable: Configurable analytics script for synthetic hospital data (Challenge 10)

This pipeline delivers a flexible script-based analysis of hospital visit records, allowing team members or automation tools to control outputs using a JSON config file or CLI flags. It generates both summary data and a department-level cost visualization.

---

## 🎯 Project Objectives

- ✅ Accept runtime configuration via `config/default_config.json`
- ✅ Allow CLI-based overrides: `--save`, `--no-save`, `--plot`, `--no-plot`
- ✅ Export key deliverables (CSV + department cost chart)
- ✅ Ready-to-run script (`cli.py`) + modular analytics logic (`pipeline/core.py`)

---

## 🩺 Data Schema

Each generated record represents a hospital visit in 2023 and includes:

| Column       | Description                                  |
|--------------|----------------------------------------------|
| `visit_date` | Date of the hospital visit                   |
| `department` | Department name (e.g., Cardiology, Oncology) |
| `diagnosis`  | Diagnosis keyword (e.g., Hypertension, Asthma)|
| `patient_id` | Anonymized ID                                |
| `age_group`  | Age bucket (`0-17`, `18-35`, etc.)            |
| `gender`     | `Male` / `Female`                            |
| `cost`       | Total visit cost in Euros                    |

---

## 🧩 Your Core Tasks

| Task                                     | What to Do                                                           | File / Location               |
|------------------------------------------|----------------------------------------------------------------------|-------------------------------|
| 🟩 Run the pipeline                      | Test with default config: `python cli.py --config config/default_config.json` | Terminal                      |
| 🟩 Test CLI overrides                   | Try `--plot`, `--no-save`, etc. See if overrides apply correctly     | `cli.py`                      |
| 🟩 Inspect output files                 | Check for: `output/hospital_visits.csv` and `output/cost_by_department.png` | `output/` folder              |
| 🟩 Explore the CSV                      | Open in pandas or Excel. Try grouping by diagnosis, department, etc. | Your analysis notebook        |
| 🟩 Write summary insights               | What does the data or plot reveal? Write 2–3 bullets of real meaning | Print, report, or README.md   |
| 🟩 Add 1–2 basic tests                  | Use `os.path.exists()` to confirm CSV or plot created in `test_cli.py` | `tests/test_cli.py`          |

---

## 🟡 Stretch Goals (Optional, but Recommended)

| Goal                          | Why It Matters                                                       | Hint / Tool                     |
|-------------------------------|------------------------------------------------------------------------|----------------------------------|
| 🟡 Add `YAML` config support  | YAML is common in pipelines, Airflow, CI tools                         | Use `pyyaml`                    |
| 🟡 Add logging                | Replace `print()` with `logging.info()` and configure output           | Python `logging` module         |
| 🟡 Modularize `core.py`       | Separate into `generate_data()`, `analyze()`, `export()`               | Better for scaling/reuse        |
| 🟡 Use real CSV instead       | Allow the pipeline to load a real `hospital_data.csv` if available     | `pd.read_csv(path)`             |
| 🟡 Add seasonal visual        | Show monthly total cost or visit volume (e.g., line chart)             | `df['visit_date'].groupby()`    |
| 🟡 Add `--output-dir` flag    | Let CLI override `output_dir` from config                              | Add `--output-dir` in argparse  |
| 🟡 Add CLI mode summary       | Print a "mode summary" at the end: what was saved and where            | Use `.format()` or f-strings    |

---

## 📊 Outputs

By default, the pipeline generates:

- `output/hospital_visits.csv`: Full dataset (400+ rows)
- `output/cost_by_department.png`: Horizontal bar chart of total visit cost per department

---

## 🛠️ How to Run

### ✅ Option 1 – Use Config File
```bash
python cli.py --config config/default_config.json
```

### ✅ Option 2 – Override Behavior via CLI
```bash
python cli.py --config config/default_config.json --no-save --plot
```

---

## 🟡 Deploy and Schedule Like a Production Pipeline (Advanced Stretch Goals)

| Goal                                | Why It Matters                                                           | Tools / Simulations              |
|-------------------------------------|---------------------------------------------------------------------------|----------------------------------|
| 🟡 **Dockerize the pipeline**       | Simulates deployment to Cloud Run, ECS, or container-based infrastructure | `Dockerfile`, `run.sh`           |
| 🟡 **Run via cron job**             | Mimics local or Linux server scheduling of data workflows                | `cron-example.txt`               |
| 🟡 **Add CI/CD with GitHub Actions**| Run pipeline daily or on push — great for automated data refresh         | `.github/workflows/main.yml`     |
| 🟡 **Use shell flags in container** | Simulates runtime overrides (e.g., plot/save behavior in cloud tasks)    | `run.sh`, Docker `CMD` arguments |

---

### ✅ Learning Outcome
By completing these, you're simulating how real data workflows are:

- **Containerized** for portability
- **Scheduled** for automation
- **Triggered by events** via CI/CD

These stretch goals help transition your pipeline from *"runs on my machine"* to *"deployable, reusable, and automated"* — like a true medior engineer.
