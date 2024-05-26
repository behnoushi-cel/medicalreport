from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from assignments.model.entity.base import Base
from assignments.model.entity.patient import Patient
from assignments.model.entity.doctor import Doctor
from assignments.model.entity.medical_report import MedicalReport

from assignments.model.tools.validator import Validator