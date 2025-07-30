# Data Analysis & Engineering Challenges

This repository features a collection of standalone tasks and small-scale projects centered around data analysis and engineering workflows. Each entry includes a dataset, a business-style prompt, and a complete solution implemented in Python.

---

## Purpose

The aim is to develop a well-structured, practical archive of real-world data challenges with a focus on:

- Working with raw and semi-structured data
- Exploring, cleaning, and transforming datasets
- Building lightweight ETL pipelines and summary reports
- Applying Python, SQL, and common data libraries
- Practicing reproducible, maintainable analysis

---

## Repository Structure

- Each folder is numbered sequentially: `challenge_01`, `challenge_02`, etc.
- Each folder contains:
  - A **task prompt** (realistic business scenario)
  - A **dataset** or external data source
  - One or more **scripts** or notebooks with the solution
  - A brief `README.md` summarizing approach and key outputs

---

## Tools & Technologies

- Python (`pandas`, `numpy`, `matplotlib`, `seaborn`, `sqlite3`)
- SQL (via SQLite or DuckDB)
- File formats: CSV, JSON
- ETL and scripting patterns
- Planned: APIs, workflow orchestration, deployment tools

---

## Challenges Completed

## Challenges Completed

| Challenge | Focus Area | Skill Focus | Status |
|----------:|------------|-------------|--------|
| 01 | Supermarket Sales EDA | Pandas – grouping, charting, visual/textual insight writing | Complete |
| 02 | Python Function Practice | LeetCode-style logic, pandas, clean syntax, edge cases | Complete |
| 03 | JSON-Like Data Parsing | Parsing semi-structured data, flattening, query building | Complete |
| 04 | Retail Data Pipeline | Modular loading, cleaning, aggregation, pipeline chaining | Complete |
| 05 | Advanced Revenue Insights | Grouped analysis, time trends, business storytelling | Complete |
| 06 | Time-Series Sales Trends | Resampling, seasonality, line-plots, moving averages | Complete |
| 07 | Margin Leakage in Clinical Supplies | Multi-source joins, margin calculations, enrichment | Complete |
| 08 | CRM & Transaction Analytics | Nested-JSON flattening, safe logic, derived fields, argparse, modularisation, pytest, logging, Makefile automation | Complete |
| 09 | Data-Validation Framework | Input/data schema validation, error handling, modularity, testing | Complete |
| 10 | Config-Driven Outputs | CLI flags, YAML/JSON configs, logging behaviours, report generation | Complete |
| 11 | Symptom-Tracker API Wrapper | OOP, JSON-API integration, reusable client design, filtering, DataFrame export | In Progress |
| 12 | Clinical-Trial Scraper | API interaction, nested-JSON normalisation, pandas, bar chart, insight writing | Complete |
| 13 | Drug Adherence Analytics | PostgreSQL, SQLAlchemy 2.x, Alembic, Docker, pandas, matplotlib | Complete |
| 14 | Clinical Log Parser | Regex parsing, text-to-JSON/CSV, validation, null handling, CLI design (optional) | Complete |
| 15 | Dynamic Drug Pricing Optimization | Vectorized pandas, conditional logic, business simulation, function design | In Progress |

---

## How to Use This Repository

### Structure

- **Each challenge** lives in its own folder:  
  `challenge_01/`, `challenge_02/`, ..., `challenge_09/`, etc.
- **Inside each folder you’ll find:**
  - `main.ipynb` or `main.py` – notebook or script for the core solution.
  - `data/` – sample datasets or download instructions.
  - `outputs/` – generated visualizations, processed files, or summary reports.
  - `validator.py` and `test_validator.py` – (from Challenge 9+) input validation and automated tests for data quality.

---

## License

MIT License. Datasets used are publicly available and credited in each challenge folder.
