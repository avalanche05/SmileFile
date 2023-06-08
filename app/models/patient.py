# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

from app.models.visit import Visit


class Patient(BaseModel):
    id: Optional[str] = Field(alias="id", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    contact_details: Optional[str] = Field(alias="contactDetails", default=None)
    last_appointment: Optional[datetime] = Field(alias="lastAppointment", default=None)
    visits: Optional[List[Visit]] = Field(alias="visits", default=None)


class NewPatient(BaseModel):
    name: Optional[str] = Field(alias="name", default=None)
    contact_details: Optional[str] = Field(alias="contactDetails", default=None)
    last_appointment: Optional[datetime] = Field(alias="lastAppointment", default=None)
    visits: Optional[List[Visit]] = Field(alias="visits", default=None)
