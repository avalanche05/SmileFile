from datetime import datetime
from pony.orm import PrimaryKey, Required, Optional, Set

from app.main import db
from app.models.database import Visit


class Patient(db.Entity):
    id = PrimaryKey(str)
    name = Required(str)
    contact_details = Required(str)
    last_appointment = Optional(datetime)
    visits = Set(Visit)
