
from sqlalchemy import Column, Integer, String, Boolean

from model.entity.base import Base


class Doctor(Base):
    __tablename__ = "doctor_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    skill  = Column(String(30), nullable=False)
    medicalreport = relationship(medicalreport, backref="doctor")

    def __init__(self, name, family, skill):
        self.person_id = None
        self.name = name
        self.family = family
        self.skill = skill

