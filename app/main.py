# coding: utf-8
import uvicorn
from fastapi import FastAPI

from app.api.api_v1.patients import patients_router
from app.api.api_v1.visits import visits_router
import app.database.models as db_models

app = FastAPI(
    title="SmileFile",
    description="Backend for dentist application",
    version="1.0.0",
)
app.include_router(patients_router)
app.include_router(visits_router)

db_models.database.connect()
db_models.database.create_tables([db_models.Visit, db_models.Patient])

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
