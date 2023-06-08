# coding: utf-8
import uvicorn
from fastapi import FastAPI, APIRouter
from pony.orm import Database

db = Database()
router = APIRouter()
app = FastAPI(
    title="SmileFile",
    description="Backend for dentist application",
    version="1.0.0",
)
app.include_router(router)

db.bind(provider='sqlite', filename='main.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
uvicorn.run(app, host="127.0.0.1", port=8000)
