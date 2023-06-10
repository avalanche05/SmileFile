# coding: utf-8
import datetime
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

import app.database.models as db_models
from app import services
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
async def visits_get(offset: Optional[int] = 0,
                     limit: Optional[int] = 1000,
                     date: Optional[str] = None) -> List[Visit]:
    if date:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    visits = services.database.get_all_visits(offset, limit, date)
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
        visit = services.database.get_visit(visitId)
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
        visit.id = visitId
        visit = services.database.update_visit(visit)
        return visit
    except db_models.Visit.DoesNotExist:
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
    visit = services.database.create_visit(new_visit)
    return visit
