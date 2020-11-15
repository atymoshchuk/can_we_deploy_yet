import uuid
import structlog

# This example is taken from https://www.structlog.org/en/stable/index.html
# For more examples and information, check official documentation of structlog


logger = structlog.get_logger()

structlog.configure(
    processors=[
        structlog.processors.KeyValueRenderer(
            key_order=["event", "trace_id"],
        ),
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
)


log = logger.bind(trace_id=str(uuid.uuid4()))
log.error("user logged in", user="test-user")
