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
        try:
            c = a / b
        except ZeroDivisionError as e:
            logger.error("Division by zero. Check the value of b.")
            raise e

        return c

    @staticmethod
    def sum_range(a, b):
        c = 0
        for i in range(a, b + 1):
            c = Calculator.add(i, c)
        return c
