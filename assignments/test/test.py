from datetime import datetime

from assignments.controller import PatientController
from assignments.model.bl.patient_bl import PatientBl
from assignments.model.da.da import DataAccess
# Entity Test
from assignments.model.entity import *

# print(PatientController.save("co", "er"))
# patient = Patient("aaaa", "bbbb")
# PatientBl.save(patient)
# patient_da = DataAccess(Patient)
# print(patient_da.find_all())
# patient_da.save(patient)
# print(patient)
#
# doctor = Doctor("reza","rezaii", "heart")
# doctor_da = DataAccess(Doctor)
# print(doctor_da.find_all())
# doctor_da.save(doctor)
# print(doctor)

# patient = patient_da.find_by_id(1)
# doctor = doctor_da.find_by_id(1)

# med = MedicalReport(patient, doctor,datetime.now(), "description22")
# med_da = DataAccess(MedicalReport)
# print(med_da.find_all())
# med_da.save(med)
# print(med)
