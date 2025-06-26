# symptom_entry.py

# Define your SymptomEntry class here
# Example fields: date, symptoms, severity, notes

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class SymptomEntry:
    date: datetime
    symptoms: list[str]
    severity: int
    notes: Optional[str] = None
