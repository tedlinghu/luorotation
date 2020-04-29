import config
import sql_db
import pandas as pd


query = sql_db.query_schema + """
select apacheApsVar.sodium, 
vitalPeriodic.heartRate, 
vitalPeriodic.respiration, 
carePlanCareProvider.activeUponDischarge, 
patient.patientUnitStayID,
patient.gender, 
patient.age, 
patient.ethnicity, 
patient.unitDischargeStatus, 
patient.admissionHeight, 
patient.admissionWeight
from eicu_crd.patient
join eicu_crd.apacheapsvar on apacheapsvar.patientunitstayid = patient.patientunitstayid 
join eicu_crd.vitalperiodic on vitalperiodic.patientunitstayid = patient.patientunitstayid 
join eicu_crd.careplancareprovider on careplancareprovider.patientunitstayid = patient.patientunitstayid
limit 10000;
"""




patient_vital = sql_db.query_schema + """
select * from eicu_crd.patient, eicu_crd.vitalPeriodic
where patient.patientunitstayid = vitalperiodic.patientunitstayid
limit 50000;
"""


patient_apache = sql_db.query_schema + """
select * from eicu_crd.patient, eicu_crd.apacheApsVar
where patient.patientunitstayid = apacheapsvar.patientunitstayid
limit 50000;
"""



'''
query = sql_db.query_schema + """
select hospital.region, carePlanCareProvider.activeUponDischarge, patient.patientUnitStayID,
patient.gender, patient.age, patient.ethnicity, patient.unitDischargeStatus
from eicu_crd.carePlanCareProvider, eicu_crd.patient, eicu_crd.hospital
where patient.patientunitstayid = careplancareprovider.patientunitstayid and patient.hospitalid = hospital.hospitalid
limit 50000;
"""

'''