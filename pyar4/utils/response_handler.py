from pyar4.logging.logger import Logger
from pyar4.utils.dataclasses import ControllerResponse


class ResponseHandler:
    def __init__(self, logger: Logger):
        self._logger = logger

    def _str_to_response(self, response: str):
        raise NotImplementedError

    def _handle_response(self, response: ControllerResponse):
        match response.type:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                pass
