import logging

import structlog

logger_structlog = structlog.get_logger()
logger_standard = logging.getLogger()
logging.basicConfig(level=logging.INFO)

logger_structlog.info(
    "Hello Pythonista!",
    key_id="1234",
    conference_name="Awesome Conference",
    talk_name="Production ready code",
)
logger_standard.info(
    "Hello Pythonista! Conference name %s, talk name %s, key_id = %s"
    % ("Awesome Conference", "Can we deploy yet?", "1234")
)
