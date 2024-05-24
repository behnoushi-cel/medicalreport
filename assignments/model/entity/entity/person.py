
from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base


class Patient(Base):
    __tablename__ = "patient_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    medicalreport = relationship(medicalreport, backref="patient")

    def __init__(self, name, family):
        self.person_id = None
        self.name = name
        self.family = family

