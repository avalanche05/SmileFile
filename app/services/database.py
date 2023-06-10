import datetime
from typing import List

from peewee import fn

from app.models.patient import Patient, NewPatient
import app.database.models as db_models
from app.models.visit import Visit, NewVisit


def get_patient(patient_id: int) -> Patient:
    db_patient = db_models.Patient.get(db_models.Patient.id == patient_id)

    patient = Patient()
    patient.id = db_patient.id
    patient.name = db_patient.name
    patient.contact_details = db_patient.contactDetails
    patient.last_appointment = db_patient.lastAppointment
    patient.visits = db_visits_to_visits(db_patient.visits)

    return patient


def update_patient(patient: Patient) -> Patient:
    db_patient = db_models.Patient.get(db_models.Patient.id == patient.id)
    db_patient.name = patient.name
    db_patient.contactDetails = patient.contact_details
    db_patient.lastAppointment = patient.last_appointment
    db_patient.save()

    return db_patient_to_patient(db_patient)


def create_patient(new_patient: NewPatient) -> Patient:
    db_patient = db_models.Patient()
    db_patient.name = new_patient.name
    db_patient.contactDetails = new_patient.contact_details
    db_patient.lastAppointment = new_patient.last_appointment
    db_patient.save()
    db_patient.visits = create_visits(new_patient.visits, patient_id=db_patient.id)

    return db_patient_to_patient(db_patient)


def db_patient_to_patient(db_patient: db_models.Patient) -> Patient:
    patient = Patient()
    patient.id = db_patient.id
    patient.name = db_patient.name
    patient.contact_details = db_patient.contactDetails
    patient.last_appointment = db_patient.lastAppointment
    patient.visits = db_visits_to_visits(db_patient.visits)

    return patient


def get_all_patients(offset: int = 0, limit: int = 1000) -> List[Patient]:
    patients = []
    for db_patient in db_models.Patient.select() \
            .offset(offset) \
            .limit(limit):
        patients.append(db_patient_to_patient(db_patient))

    return patients


def db_visit_to_visit(db_visit: db_models.Visit) -> Visit:
    visit = Visit()

    visit.id = db_visit.id
    visit.patient_id = db_visit.patient_id
    visit.date = db_visit.date
    visit.diagnosis = db_visit.diagnosis
    visit.treatment = db_visit.treatment

    return visit


def db_visits_to_visits(db_visits: List[db_models.Visit]) -> List[Visit]:
    if not db_visits:
        return []

    visits = []

    for db_visit in db_visits:
        visit = db_visit_to_visit(db_visit)
        visits.append(visit)
    return visits


def create_visits(new_visits: List[NewVisit], patient_id: int) -> List[Visit]:
    visits = []
    for new_visit in new_visits:
        new_visit.patient_id = patient_id
        visits.append(create_visit(new_visit))

    return visits


def create_visit(new_visit: NewVisit) -> Visit:
    db_visit = db_models.Visit()
    db_visit.patient_id = new_visit.patient_id
    db_visit.date = new_visit.date
    db_visit.diagnosis = new_visit.diagnosis
    db_visit.treatment = new_visit.treatment

    db_visit.save()
    return db_visit_to_visit(db_visit)


def update_visit(visit: Visit) -> Visit:
    db_visit = db_models.Visit.get(db_models.Visit.id == visit.id)
    if visit.patient_id:
        db_visit.patient = visit.patient_id
    db_visit.date = visit.date
    db_visit.diagnosis = visit.diagnosis
    db_visit.treatment = visit.treatment
    db_visit.save()

    return db_visit_to_visit(db_visit)


def get_visit(visit_id: int) -> Visit:
    db_visit = db_models.Visit.get(db_models.Visit.id == visit_id)
    return db_visit_to_visit(db_visit)


def get_all_visits(offset: int = 0, limit: int = 1000, date: datetime.datetime = None) -> List[Visit]:
    visits = []

    if date:
        db_visits = db_models.Visit.select() \
            .where(fn.Date(db_models.Visit.date) == fn.Date(date)) \
            .order_by(db_models.Visit.date) \
            .offset(offset) \
            .limit(limit)
    else:
        db_visits = db_models.Visit.select() \
            .order_by(db_models.Visit.date) \
            .offset(offset) \
            .limit(limit)
    for db_visit in db_visits:
        visits.append(db_visit_to_visit(db_visit))

    return visits
