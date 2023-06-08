from datetime import datetime

from pony.orm import Required, PrimaryKey

from app.main import db
from app.models.database.patient import Patient


class Visit(db.Entity):
    id = PrimaryKey(str)
    date = Required(datetime)
    diagnosis = Required(str)
    treatment = Required(str)
    patient = Required(Patient)
