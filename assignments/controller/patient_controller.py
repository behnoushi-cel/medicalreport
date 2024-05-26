from assignments.model.bl.patient_bl import PatientBl
from assignments.model.entity import Patient
from assignments.model.tools.decorators import exception_handling


class PatientController:
    @staticmethod
    @exception_handling
    def save(name, family):
        patient = Patient(name, family)
        return True, PatientBl.save(patient)

    @staticmethod
    @exception_handling
    def edit(id, name, family, status=True):
        patient = Patient( name, family)
        patient.id = id
        return True, PatientBl.edit(patient)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, PatientBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, PatientBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, PatientBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, PatientBl.find_by_family(family)