import logging
import os
from datetime import datetime
from pathlib import Path

class Logger():
    def __init__(self, _config: dict):
        self._config = _config

        dir_name = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        log_dir = os.path.join(dir_name, self._config['log_dir'])
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_dir, f"{self._config['name']}_{timestamp}.log")

        self.logger = logging.getLogger(self._config['name'])
        self.logger.setLevel(logging.DEBUG)

        #Prevent duplicate handlers if multiple instances are created
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)


    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warn(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)