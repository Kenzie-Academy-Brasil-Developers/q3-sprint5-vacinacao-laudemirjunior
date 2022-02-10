from dataclasses import dataclass
from datetime import datetime
from unicodedata import name
from sqlalchemy import Column, String, DateTime
from app.configs.database import db
from datetime import datetime, timedelta

@dataclass
class Vaccine(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str
 
    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime, default=datetime.utcnow())
    second_shot_date = Column(DateTime, default=(datetime.utcnow() + timedelta(days=90)))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)