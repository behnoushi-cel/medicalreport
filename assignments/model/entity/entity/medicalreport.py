from model.entity.medicalreport import MedicalReport
from model.entity.base import Base

class MedicalReport(Base):
    __tablename__ = "medical_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patient_tbl.id"))
    doctor_id = Column(Integer, ForeignKey("doctor_tbl.id"))
    description  = Column(String(30), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))
    medical_id = Column(Integer, ForeignKey("medical"))
    medical_report =relationship("MedicalReport")

    patient = relationship(Patient)
    doctor = relationship(Doctor)

    def __init__(self,id,patient, doctor, description):
        self.person_id = None
        self.date_time = none
        self.patient = patient
        self.doctor = doctor
        self.description = description

    def get_medical_id(self):
        return self._medical_id

    def set_medical_id(self,medical_id):
        if medical_id is not None:
