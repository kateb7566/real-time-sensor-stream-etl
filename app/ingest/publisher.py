import redis.asyncio as redis
from app.ingest.models import SensorData
from app.utils.logger import get_logger

logger = get_logger(__name__)

REDIS_CHANNEL = "sensor:stream"

class Publisher:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(redis_url, decode_responses=True)
    
    async def publish(self, data: SensorData) -> None:
        try:
            await self.redis.publish(REDIS_CHANNEL, data.json())
            await self.redis.close()
            logger.info(f"Message published to channel '{data}'")
        except redis.RedisError as e:
            logger.error(f"Failed to publish to Redis: {e}")
            

publisher = Publisher()