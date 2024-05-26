# todo : complete file
from assignments.model import *


class DoctorController:
    @classmethod
    @staticmethod
    @exception_handling
    def save(name, family, skill):
        doctor = Doctor(name,family,skill)
        DoctorBl.save(doctor)