from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)

logger.add(
    "historical_platform.log",
    rotation="100 MB",
    retention="10 days",
    compression="zip"
)
