import datetime
import logging
import sys
import structlog

# This example is taken from https://www.structlog.org/en/stable/index.html
# For more examples and information, check official documentation of structlog

logging.basicConfig(stream=sys.stdout, format="%(message)s", level=logging.INFO)


def add_timestamp(_, __, event_dict):
    event_dict["timestamp"] = datetime.datetime.utcnow()
    return event_dict


def censor_password(_, __, event_dict):
    pw = event_dict.get("password")
    if pw:
        event_dict["password"] = "*CENSORED*"
    return event_dict


log = structlog.wrap_logger(
    logging.getLogger(__name__),
    processors=[
        add_timestamp,
        censor_password,
        structlog.processors.JSONRenderer(indent=2, sort_keys=True),
    ],
)
log.warning("something", password="secret")
