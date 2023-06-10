# coding: utf-8

from typing import Dict, List, Optional  # noqa: F401

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

from app import services
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
async def patients_get(offset: Optional[int] = 0, limit: Optional[int] = 1000) -> List[Patient]:
    patients = services.database.get_all_patients(offset, limit)
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
        patientId: int,
) -> Patient:
    try:
        patient = services.database.get_patient(patientId)
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
        patient.id = patientId
        return services.database.update_patient(patient)
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
    patient = services.database.create_patient(new_patient)
    return patient
