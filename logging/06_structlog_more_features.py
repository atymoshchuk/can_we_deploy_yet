import structlog
import logging

AWESOME_CONF = 35
structlog.stdlib.AWESOME_CONF = AWESOME_CONF
structlog.stdlib._NAME_TO_LEVEL["awesome_conf"] = AWESOME_CONF
structlog.stdlib._LEVEL_TO_NAME[AWESOME_CONF] = "awesome_conf"
logging.addLevelName(AWESOME_CONF, "awesome_conf")


def awesome_conf(self, msg, *args, **kw):
    return self.log(AWESOME_CONF, msg, *args, **kw)


structlog.stdlib._FixedFindCallerLogger.awesome_conf = awesome_conf
structlog.stdlib.BoundLogger.awesome_conf = awesome_conf

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.ExceptionPrettyPrinter(),  # this processor will process and beautify exceptions
        structlog.processors.JSONRenderer(indent=2, sort_keys=True),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


my_logger = structlog.get_logger("test")
try:
    raise Exception("TEST!")
except Exception:
    my_logger.exception("Exception occurred")

my_logger.awesome_conf("Hello Pythonista!")
