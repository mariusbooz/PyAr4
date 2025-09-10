import logging
import os
from datetime import datetime
from pathlib import Path


class FileLogger:
    """
    Simple logging class to handle logging to a file.

    Attributes:
        _logger(Logger) : Logger object, owns the file handle and writes to it.
    """

    def __init__(self, _dir_name: str):
        parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        log_dir = os.path.join(parent_dir_name, _dir_name)
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_dir, f"PyAr4_{timestamp}.log")

        self._logger = logging.getLogger(self._config["name"])
        self._logger.setLevel(logging.DEBUG)

        # Prevent duplicate handlers if multiple instances are created
        if not self._logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)

            self._logger.addHandler(file_handler)

    def info(self, msg: str) -> None:
        """
        Log a given message with the tag [info].

        Parameters:
            msg(str) : Message to be written to the file.
        """
        self._logger.info(msg)

    def warn(self, msg: str) -> None:
        """
        Log a given message with the tag [warning].

        Parameters:
            msg(str) : Message to be written to the file.
        """
        self._logger.warning(msg)

    def error(self, msg: str) -> None:
        """
        Log a given message with the tag [error].

        Parameters:
            msg(str) : Message to be written to the file.
        """
        self._logger.error(msg)

    def debug(self, msg: str) -> None:
        """
        Log a given message with the tag [debug].

        Parameters:
            msg(str) : Message to be written to the file.
        """
        self._logger.debug(msg)
