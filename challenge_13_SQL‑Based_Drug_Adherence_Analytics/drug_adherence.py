# drug_adherence.py
import pandas as pd
from datetime import datetime
from db import SessionLocal, engine
from models import Refill, Base
import sys
from analytics import (
    get_average_refill_interval,
    get_late_refills,
    top_3_drugs,
    adherence_rate_by_drug)

Base.metadata.create_all(bind=engine)

def load_csv_to_db(csv_path: str):
    df = pd.read_csv(csv_path, parse_dates=["refill_date"])
    print(f"Loaded {len(df)} rows")

    with SessionLocal() as session:
        for _, row in df.iterrows():
            refill = Refill(
                patient_id=row["patient_id"],
                drug=row["drug"],
                refill_date=row["refill_date"].date()  # convert Timestamp to date
            )
            session.add(refill)

        session.commit()
        print("All rows inserted into database.")


if __name__ == "__main__":
    csv_path = sys.argv[1]
    load_csv_to_db(csv_path)
    get_average_refill_interval()
    get_late_refills()
    top_3_drugs()
    adherence_rate_by_drug()