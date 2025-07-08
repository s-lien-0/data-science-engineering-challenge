from sqlalchemy import text
from db import SessionLocal
import pandas as pd
from settings import DEFAULT_INTERVAL_DAYS, GRACE_PERCENT
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

def get_average_refill_interval():
    query = text("""
        WITH diffs AS (
            SELECT
                patient_id,
                refill_date,
                LEAD(refill_date) OVER (
                    PARTITION BY patient_id
                    ORDER BY refill_date
                ) AS next_refill
            FROM refills
        )
        SELECT
            patient_id,
            ROUND(AVG(next_refill - refill_date), 2) AS avg_interval
        FROM diffs
        WHERE next_refill IS NOT NULL
        GROUP BY patient_id
        ORDER BY patient_id;
    """)

    with SessionLocal() as session:
        df = pd.read_sql(query, session.bind)
        print("\nAverage refill interval per patient:")
        print(df)

        df.to_csv("outputs/average_refill_interval.csv", index=False)
        print("Saved to outputs")

    
def get_late_refills():
    grace_days = DEFAULT_INTERVAL_DAYS * (1 + GRACE_PERCENT)

    query = text(f"""
        WITH diffs AS (
            SELECT
                patient_id,
                drug,
                refill_date,
                LEAD(refill_date) OVER (
                    PARTITION BY patient_id, drug
                    ORDER BY refill_date
                ) AS next_refill
            FROM refills
        ),
        gaps AS (
            SELECT
                patient_id,
                drug,
                refill_date,
                next_refill,
                (next_refill - refill_date) AS gap_days
            FROM diffs
            WHERE next_refill IS NOT NULL
        )
        SELECT
            patient_id,
            drug,
            refill_date,
            next_refill,
            gap_days,
            CASE WHEN gap_days > :grace THEN 1 ELSE 0 END AS is_late
        FROM gaps
        ORDER BY patient_id, refill_date;
    """)

    with SessionLocal() as session:
        df = pd.read_sql(query, session.bind, params={"grace": grace_days})
        print(f"\nLate refill flags (grace = {grace_days:.1f} days):")
        print(df[df["is_late"] == 1])

        df.to_csv("outputs/late_refills.csv", index=False)
        print("Saved to outputs")

def top_3_drugs():
    query = text("""
        SELECT
            drug,
            COUNT(*) AS refill_count
        FROM refills
        GROUP BY drug
        ORDER BY refill_count DESC
        LIMIT 3;
    """)

    with SessionLocal() as session:
        df = pd.read_sql(query, session.bind)
        print("\nTop 3 drugs by refill count:")
        print(df)

        df.to_csv("outputs/top_3_drugs.csv", index=False)

def adherence_rate_by_drug():
    query = text("""
        WITH diffs AS (
            SELECT patient_id, drug, refill_date,
                   LEAD(refill_date) OVER (
                       PARTITION BY patient_id, drug
                       ORDER BY refill_date
                   ) AS next_refill
            FROM refills
        ),
        gaps AS (
            SELECT patient_id, drug, refill_date, next_refill,
                   (next_refill - refill_date) AS gap_days
            FROM diffs
            WHERE next_refill IS NOT NULL
        )
        SELECT
            drug,
            COUNT(*) AS total_refills,
            SUM(CASE WHEN (next_refill - refill_date) <= :grace THEN 1 ELSE 0 END) AS on_time
        FROM gaps
        GROUP BY drug
    """)

    from settings import DEFAULT_INTERVAL_DAYS, GRACE_PERCENT
    grace = DEFAULT_INTERVAL_DAYS * (1 + GRACE_PERCENT)

    with SessionLocal() as session:
        df = pd.read_sql(query, session.bind, params={"grace": grace})
        df["adherence_rate"] = (df["on_time"] / df["total_refills"]) * 100

    plt.figure(figsize=(8, 5))
    plt.bar(df["drug"], df["adherence_rate"])
    plt.ylabel("Adherence Rate (%)")
    plt.title("On-Time Refill Rate by Drug")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/adherence_by_drug.png")
    print("\nAdherence chart saved to outputs/adherence_by_drug.png")
