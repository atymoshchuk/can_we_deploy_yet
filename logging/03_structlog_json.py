import structlog
import logging

EUROPYTHON = 35
structlog.stdlib.EUROPYTHON = EUROPYTHON
structlog.stdlib._NAME_TO_LEVEL["europython"] = EUROPYTHON
structlog.stdlib._LEVEL_TO_NAME[EUROPYTHON] = "europython"
logging.addLevelName(EUROPYTHON, "europython")

def europython(self, msg, *args, **kw):
    return self.log(EUROPYTHON, msg, *args, **kw)

structlog.stdlib._FixedFindCallerLogger.europython = (
    europython
)
structlog.stdlib.BoundLogger.europython = europython

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
        structlog.processors.JSONRenderer(indent=2, sort_keys=True)
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


my_logger = structlog.get_logger("test")

my_logger.europython("Hello Pythonista!")
