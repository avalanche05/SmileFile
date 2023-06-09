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

import app.database.models as db_models
from app.models.visit import Visit, NewVisit

visits_router = APIRouter()


@visits_router.get(
    "/visits",
    responses={
        200: {"model": List[Visit], "description": "Список посещений"},
    },
    tags=["default"],
    summary="Получить список всех посещений",
    response_model_by_alias=True,
)
async def patients_get(
) -> List[Visit]:
    visits = []
    for db_visit in db_models.Visit.select():
        visit = Visit()
        visit.id = db_visit.id
        visit.patient_id = db_visit.patient.id
        visit.date = db_visit.date
        visit.diagnosis = db_visit.diagnosis
        visit.treatment = db_visit.treatment

        visits.append(visit)
    return visits


@visits_router.get(
    "/visits/{visitId}",
    responses={
        200: {"model": Visit, "description": "Информация о посещении"},
    },
    tags=["default"],
    summary="Получить конкретноое посещение",
    response_model_by_alias=True,
)
async def visit_id_get(
        visitId: str,
) -> Visit:
    try:
        db_visit = db_models.Visit.get(db_models.Visit.id == visitId)

        visit = Visit()
        visit.id = db_visit.id
        visit.patient_id = db_visit.patient.id
        visit.date = db_visit.date
        visit.diagnosis = db_visit.diagnosis
        visit.treatment = db_visit.treatment

        return visit
    except db_models.Visit.DoesNotExist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": f"Visit with id = {visitId} not found."})


@visits_router.put(
    "/visits/{visitId}",
    responses={
        200: {"model": Visit, "description": "Информация о посещении обновлена"},
    },
    tags=["default"],
    summary="Обновить информацию о посещении",
    response_model_by_alias=True,
)
async def patients_patient_id_put(
        visitId: str,
        visit: Visit = Body(None, description=""),
) -> Visit:
    try:
        db_visit = db_models.Visit.get(db_models.Visit.id == visitId)

        db_visit.patient_id = visit.patient_id
        db_visit.date = visit.date
        db_visit.diagnosis = visit.diagnosis
        db_visit.treatment = visit.treatment

        db_visit.save()

        visit = Visit()
        visit.id = db_visit.id
        visit.patient_id = db_visit.patient.id
        visit.date = db_visit.date
        visit.diagnosis = db_visit.diagnosis
        visit.treatment = db_visit.treatment

        return visit
    except db_models.Patient.DoesNotExist:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": f"Visit with id = {visitId} not found."})


@visits_router.post(
    "/visits",
    responses={
        201: {"model": Visit, "description": "Посещение создано"},
    },
    tags=["default"],
    summary="Добавить новое посещение",
    response_model_by_alias=True,
)
async def patients_post(
        new_visit: NewVisit = Body(None, description=""),
) -> Visit:
    db_visit = db_models.Visit()
    db_visit.patient = new_visit.patient_id
    db_visit.date = new_visit.date
    db_visit.diagnosis = new_visit.diagnosis
    db_visit.treatment = new_visit.treatment

    db_visit.save()

    visit = Visit()
    visit.id = db_visit.id
    visit.patient_id = db_visit.patient.id
    visit.date = db_visit.date
    visit.diagnosis = db_visit.diagnosis
    visit.treatment = db_visit.treatment
    return visit
