import structlog

logger_structlog = structlog.get_logger(__name__)

logger_structlog = logger_structlog.bind(
    key_id="1234", conference_name="Awesome Conference", talk_name="Can we deploy yet?"
)
try:
    raise Exception("Oh, something went wrong...")
except Exception:
    logger_structlog.exception("logging exception")

logger_structlog.info("Some info")
