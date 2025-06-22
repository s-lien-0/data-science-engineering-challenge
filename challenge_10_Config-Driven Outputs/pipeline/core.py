import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def run_pipeline(save_csv=True, generate_plot=False, output_dir="output"):
    import random
    from datetime import timedelta

    def random_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # Generate synthetic hospital data
    n_rows = 400
    random.seed(42)
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    departments = ['Cardiology', 'Oncology', 'Neurology', 'Orthopedics', 'General Medicine', 'Pediatrics']
    diagnoses = ['Hypertension', 'Diabetes', 'Cancer', 'Fracture', 'Migraine', 'Fever', 'Asthma']
    genders = ['Male', 'Female']
    age_groups = ['0-17', '18-35', '36-55', '56-75', '75+']

    data = []
    for _ in range(n_rows):
        visit_date = random_date(start_date, end_date)
        department = random.choice(departments)
        diagnosis = random.choice(diagnoses)
        patient_id = f"P{random.randint(1000, 9999)}"
        age_group = random.choices(age_groups, weights=[0.1, 0.3, 0.3, 0.2, 0.1])[0]
        gender = random.choice(genders)
        cost = round(random.uniform(50, 5000), 2)
        data.append({
            "visit_date": visit_date.date(),
            "department": department,
            "diagnosis": diagnosis,
            "patient_id": patient_id,
            "age_group": age_group,
            "gender": gender,
            "cost": cost
        })

    df = pd.DataFrame(data)

    if save_csv:
        os.makedirs(output_dir, exist_ok=True)
        df.to_csv(f"{output_dir}/hospital_visits.csv", index=False)
        print(f"✅ Saved hospital data to {output_dir}/hospital_visits.csv")

    if generate_plot:
        # Plot: Total cost by department
        plt.figure(figsize=(10, 6))
        df.groupby("department")["cost"].sum().sort_values().plot(kind="barh")
        plt.title("💰 Total Visit Cost by Department")
        plt.xlabel("Total Cost (€)")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/cost_by_department.png")
        print(f"📊 Saved plot to {output_dir}/cost_by_department.png")

    return df
