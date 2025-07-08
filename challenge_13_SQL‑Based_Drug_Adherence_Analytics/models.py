# models.py

from sqlalchemy import Column, Integer, String, Date
from db import Base

class Refill(Base):
    __tablename__ = "refills"

    id          = Column(Integer, primary_key=True, index=True)
    patient_id  = Column(String, nullable=False)
    drug        = Column(String, nullable=False)
    refill_date = Column(Date, nullable=False)
