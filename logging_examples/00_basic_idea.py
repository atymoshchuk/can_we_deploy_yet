import logging

my_logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

my_logger.info(
    "Hello Pythonista! Conference name %s, talk name %s, key_id = %s"
    % ("Awesome Conference", "Production checklist", "1234")
)
