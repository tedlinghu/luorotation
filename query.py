import config
import sql_db
import pandas as pd

query = sql_db.query_schema + """
select hospital.region, carePlanCareProvider.activeUponDischarge, patient.patientUnitStayID,
patient.gender, patient.age, patient.ethnicity, patient.unitDischargeStatus
from eicu_crd.carePlanCareProvider, eicu_crd.patient, eicu_crd.hospital
where patient.patientunitstayid = careplancareprovider.patientunitstayid and patient.hospitalid = hospital.hospitalid
limit 50000;
"""

'''


query = sql_db.query_schema + """
select hospital.region

from eicu_crd.hospital

limit 200;
"""

'''