from app.models.schemas import SensorData
from app.models.entities import SensorRecord

def sensor_schema_to_entity(schema: SensorData) -> SensorRecord:
    return SensorRecord(
        sensor_id = schema.sensor_id,
        type = schema.type,
        value = schema.value,
        timestamp = schema.timestamp
    )