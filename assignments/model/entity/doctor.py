from assignments.model.entity import *



class Doctor(Base):
    __tablename__ = "doctor_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    skill = Column(String(50), nullable=False)
    # todo : national_id, phone, birth_date


    medical_report = relationship("MedicalReport", back_populates="doctor")

    def __init__(self, name, family, skill):
        self.person_id = None
        self.name = name
        self.family = family
        self.skill = skill

    # todo : getter / setter (validation)