"""
    Defines basic math operations.
"""
import logging

formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.addHandler(stream_handler)


class Calculator:
    """Arithmetic calculator."""

    @staticmethod
    def add(a, b):
        c = a + b

        logger.info("Add %i + %i result %i", a, b, c)
        return c

    @staticmethod
    def divide(a, b):
        pass
