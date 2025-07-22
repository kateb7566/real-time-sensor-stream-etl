import asyncio
import websockets
import random
import json
from datetime import datetime
from app.models.schemas import SensorData
from app.utils.logger import get_logger

SERVER_URL = "ws://localhost:8000/ws/sensor"
SENSOR_TYPES = ["temperature", "humidity", "pressure"]
SENSOR_IDS = ["sensor_1", "sensor_2", "sensor_3"]

logger = get_logger(__name__)

def generate_sensor_data(sensor_id: str, sensor_type: str) -> SensorData:
    # Randomize the value per sensor type
    if sensor_type == "temperature":
        value = round(random.uniform(20.0, 30.0), 2)
    elif sensor_type == "humidity":
        value = round(random.uniform(30.0, 90.0), 2)
    elif sensor_type == "pressure":
        value = round(random.uniform(950.0, 1050.0), 2)
    else:
        value = 0.0
        
    return SensorData(
        sensor_id=sensor_id,
        type=sensor_type,
        value=value,
        timestamp=datetime.utcnow().isoformat()
    )
    
async def simulate_sensor(sensor_id: str, sensor_type: str):
    try:
        async with websockets.connect(SERVER_URL) as websocket:
            while True:
                sensor_id = random.choice(SENSOR_IDS)
                sensor_type = random.choice(SENSOR_TYPES)
                data = generate_sensor_data(sensor_id, sensor_type)
                await websocket.send(data.json())
                logger.info(f"Sent data: {data}")
                await asyncio.sleep(random.uniform(1, 5))  # Random delay between messages
    except Exception as e:
        logger.error(f"Error in sensor simulation for {sensor_id}: {e}")
        
        
async def main():
    tasks = []
    for sensor_id in SENSOR_IDS:
        for sensor_type in SENSOR_TYPES:
            tasks.append(simulate_sensor(sensor_id, sensor_type))
            
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    asyncio.run(main())
    logger.info("Sensor simulation started.")
    logger.info("Press Ctrl+C to stop the simulation.")    