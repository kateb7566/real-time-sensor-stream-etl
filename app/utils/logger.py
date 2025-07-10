# Set up the logger

# Built in imports
import logging

# Local Imports
from app.config import settings

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    log_eval = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(log_eval)
    
    # Formatting
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] → %(message)s",
                                "%Y-%m-%d %H:%M:%S")
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger