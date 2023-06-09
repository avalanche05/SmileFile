# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)
from fastapi.responses import JSONResponse

from app.models.patient import Patient, NewPatient
import app.database.models as db_models
from app.models.visit import Visit

patients_router = APIRouter()


@patients_router.get(
    "/patients",
    responses={
        200: {"model": List[Patient], "description": "Список пациентов"},
    },
    tags=["default"],
    summary="Получить список всех пациентов",
    response_model_by_alias=True,
)
async def patients_get(
) -> List[Patient]:
    patients = []
    for db_patient in db_models.Patient.select():
        patient = Patient()
        patient.id = db_patient.id
        patient.name = db_patient.name
        patient.contact_details = db_patient.contactDetails
        patient.last_appointment = db_patient.lastAppointment
        patient.visits = []
        for db_visit in db_patient.visits:
            visit = Visit()
            visit.id = db_visit.id
            visit.patient_id = db_visit.patient.id
            visit.date = db_visit.date
            visit.diagnosis = db_visit.diagnosis
            visit.treatment = db_visit.treatment

            patient.visits.append(visit)

        patients.append(patient)
    return patients


@patients_router.get(
    "/patients/{patientId}",
    responses={
        200: {"model": Patient, "description": "Информация о пациенте"},
    },
    tags=["default"],
    summary="Получить конкретного пациента",
    response_model_by_alias=True,
)
async def patients_patient_id_get(
        patientId: str,
) -> Patient:
    try:
        db_patient = db_models.Patient.get(db_models.Patient.id == patientId)

        patient = Patient()
        patient.id = db_patient.id
        patient.name = db_patient.name
        patient.contact_details = db_patient.contactDetails
        patient.last_appointment = db_patient.lastAppointment
        patient.visits = []

        for db_visit in db_patient.visits:
            visit = Visit()
            visit.id = db_visit.id
            visit.patient_id = db_visit.patient.id
            visit.date = db_visit.date
            visit.diagnosis = db_visit.diagnosis
            visit.treatment = db_visit.treatment

            patient.visits.append(visit)
        return patient
    except db_models.Patient.DoesNotExist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": f"Patient with id = {patientId} not found."})


@patients_router.put(
    "/patients/{patientId}",
    responses={
        200: {"model": Patient, "description": "Информация о пациенте обновлена"},
    },
    tags=["default"],
    summary="Обновить информацию о пациенте",
    response_model_by_alias=True,
)
async def patients_patient_id_put(
        patientId: str,
        patient: Patient = Body(None, description=""),
) -> Patient:
    try:
        db_patient = db_models.Patient.get(db_models.Patient.id == patientId)

        db_patient.name = patient.name
        db_patient.contactDetails = patient.contact_details
        db_patient.lastAppointment = patient.last_appointment
        db_patient.save()

        patient = Patient()

        patient.id = db_patient.id
        patient.name = db_patient.name
        patient.contact_details = db_patient.contactDetails
        patient.last_appointment = db_patient.lastAppointment
        patient.visits = []

        for db_visit in db_patient.visits:
            visit = Visit()
            visit.id = db_visit.id
            visit.patient_id = db_visit.patient.id
            visit.date = db_visit.date
            visit.diagnosis = db_visit.diagnosis
            visit.treatment = db_visit.treatment

            patient.visits.append(visit)

        return patient
    except db_models.Patient.DoesNotExist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": f"Patient with id = {patientId} not found."})


@patients_router.post(
    "/patients",
    responses={
        201: {"model": Patient, "description": "Пациент создан"},
    },
    tags=["default"],
    summary="Добавить нового пациента",
    response_model_by_alias=True,
)
async def patients_post(
        new_patient: NewPatient = Body(None, description=""),
) -> Patient:
    patient = Patient()

    db_patient = db_models.Patient(
        name=new_patient.name,
        contactDetails=new_patient.contact_details,
        lastAppointment=new_patient.last_appointment
    )
    db_patient.save()

    patient.id = db_patient.id
    patient.name = db_patient.name
    patient.contact_details = db_patient.contactDetails
    patient.last_appointment = db_patient.lastAppointment
    patient.visits = []

    if new_patient.visits:
        for visit in new_patient.visits:
            db_visit = db_models.Visit(
                patient=patient.id,
                date=visit.date,
                diagnosis=visit.diagnosis,
                treatment=visit.treatment
            )
            db_visit.save()

    for db_visit in db_patient.visits:
        visit = Visit()
        visit.id = db_visit.id
        visit.patient_id = db_visit.patient.id
        visit.date = db_visit.date
        visit.diagnosis = db_visit.diagnosis
        visit.treatment = db_visit.treatment

        patient.visits.append(visit)

    return patient
