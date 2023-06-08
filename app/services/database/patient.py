from pony.orm import db_session, ObjectNotFound

from app.models.patient import Patient, NewPatient

import app.models.database as db_models


@db_session
def create_patient(new_patient: NewPatient) -> Patient:
    db_patient = db_models.Patient(
        name=new_patient.name,
        contact_details=new_patient.contact_details,
        last_appointment=new_patient.last_appointment,
        visits=new_patient.visits
    )
    return Patient(
        id=db_patient.id,
        name=db_patient.name,
        contact_details=db_patient.contact_details,
        last_appointment=db_patient.last_appointment,
        visits=db_patient.visits
    )
