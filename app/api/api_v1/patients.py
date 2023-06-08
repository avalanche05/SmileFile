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

from app.main import router
from app.models.patient import Patient, NewPatient
import app.services.database as db_services


@router.get(
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
    ...


@router.get(
    "/patients/{patientId}",
    responses={
        200: {"model": Patient, "description": "Информация о пациенте"},
    },
    tags=["default"],
    summary="Получить конкретного пациента",
    response_model_by_alias=True,
)
async def patients_patient_id_get(
        patientId: str = Path(None, description=""),
) -> Patient:
    ...


@router.put(
    "/patients/{patientId}",
    responses={
        200: {"model": Patient, "description": "Информация о пациенте обновлена"},
    },
    tags=["default"],
    summary="Обновить информацию о пациенте",
    response_model_by_alias=True,
)
async def patients_patient_id_put(
        patientId: str = Path(None, description=""),
        patient: Patient = Body(None, description=""),
) -> Patient:
    ...


@router.post(
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
    print('wfowqfjq')
    return db_services.create_patient(new_patient)
