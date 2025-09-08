from abc import ABC, abstractmethod
from pyar4.utils.dataclasses import *


class BaseController(ABC):
    def __init__(self, _config: dict):
        self._is_running = False
        self._is_processing = False
        self._config = _config['hardware']
        self._position_dict: dict[str,list[float]] = {}
        self._current_position: list[float] = []
        self._joint_angles: list[float] = []
        
        self.command_dict: dict[str, callable]

    @abstractmethod
    def execute(self, cmd: Command):
        pass
    
    @abstractmethod
    def _startup(self) -> None:
        pass

