
from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base


class Patient(Base):
    __tablename__ = "patient_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)

    def __init__(self, name, family):
        self.person_id = None
        self.name = name
        self.family = family


class Doctor(Base):
    __tablename__ = "doctor_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    skill  = Column(String(30), nullable=False)

    def __init__(self, name, family, skill):
        self.person_id = None
        self.name = name
        self.family = family
        self.skill = skill


class MedicalReport(Base):
    __tablename__ = "medical_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patient_tbl.id"))
    doctor_id = Column(Integer, ForeignKey("doctor_tbl.id"))
    description  = Column(String(30), nullable=False)

    patient = relationship(Patient)
    doctor = relationship(Doctor)

    # finances = relationship("Finance")

    def __init__(self, patient, doctor, description):
        self.person_id = None
        self.patient = patient
        self.doctor = doctor
        self.description = description

