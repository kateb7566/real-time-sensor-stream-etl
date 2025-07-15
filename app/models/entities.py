from sqlalchemy import Column, Integer, String, Float, Datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SensorRecord(Base):
    __tablename__ = "sensor_records"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    type = Column(String)
    value = Column(Float)
    timestamp = Column(DateTime, index=True)