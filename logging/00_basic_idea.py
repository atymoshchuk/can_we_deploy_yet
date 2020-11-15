import logging

my_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

my_logger.info(
    "Hello Pythonista! Conference name %s, talk name %s, key_id = %s"
    % ("Awesome Conference", "Can we deploy yet?", "1234")
)
