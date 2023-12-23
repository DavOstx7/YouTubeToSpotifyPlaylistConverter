import os
import json
import logging.config

_FILE_DIR = os.path.dirname(__file__)
_CONFIG_DIR = os.path.join(_FILE_DIR, "../../../config/")


def load_config_file(filename: str):
    config_file = os.path.join(_CONFIG_DIR, filename)
    with open(config_file, "r") as file:
        return json.load(file)


def configure_logging(level: str):
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": "%(name)s : %(asctime)s : %(levelname)s : %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S"
            },
        },
        "handlers": {
            "stream": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "null": {
                "class": "logging.NullHandler",
            },
        },
        "root": {
            "handlers": ["null"]
        },
        "loggers": {
            "src": {
                "handlers": ["stream"],
                "level": level,
                "propagate": False
            }
        }
    })