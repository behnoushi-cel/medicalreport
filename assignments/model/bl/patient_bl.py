from assignments.controller.exceptions.exceptions import PatientNotFoundError
from assignments.model.da.da import DataAccess
from assignments.model.entity.patient import Patient

patient_da = DataAccess(Patient)


class PatientBl:
    @staticmethod
    def save(patient):
        return patient_da.save(patient)

    @staticmethod
    def edit(patient):
        if patient_da.find_by_id(patient.id):
            return patient_da.edit(patient)
        else:
            raise PatientNotFoundError()

    @staticmethod
    def remove(id):
        patient = patient_da.find_by_id(id)
        if patient:
            return patient_da.remove(patient)
        else:
            raise PatientNotFoundError()

    @staticmethod
    def find_all():
        patient_list = patient_da.find_all()
        if patient_list:
            return patient_list
        else:
            raise PatientNotFoundError()

    @staticmethod
    def find_by_id(id):
        patient = patient_da.find_by_id(id)
        if patient:
            return patient
        else:
            raise PatientNotFoundError()

    @staticmethod
    def find_by_family(family):
        patient_list = patient_da.find_by(Patient.family == family)
        if patient_list:
            return patient_list
        else:
            raise PatientNotFoundError()