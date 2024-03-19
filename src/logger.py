from loguru import logger as cs_logger
from sys import stderr

cs_logger.remove()
cs_logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <1}</level> | <white>{message}</white>")
