import logging
import sys

from app.config.settings import settings


def configure_logging() -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
        force=True
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return configured logger.
    """

    return logging.getLogger(name)