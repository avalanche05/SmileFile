from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Visit(BaseModel):
    id: Optional[str] = Field(alias="id", default=None)
    patient_id: Optional[str] = Field(alias="patientId", default=None)
    date: Optional[datetime] = Field(alias="date", default=None)
    diagnosis: Optional[str] = Field(alias="diagnosis", default=None)
    treatment: Optional[str] = Field(alias="treatment", default=None)
