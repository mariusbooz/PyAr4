from abc import ABC, abstractmethod


class Controller(ABC):
    """
    Abstract base class of any controller.

    Attributes:
        test(int) : 123
    """

    def __init__(self):
        self._is_running = False
        self._is_processing = False
        self._position_dict: dict[str, list[float]] = {}
        self._current_position: list[float] = []
        self._joint_angles: list[float] = []


# TODO: what is actually necessary here?
# @abstractmethod
# def execute(self, cmd: Command):
#     pass

# @abstractmethod
# def _startup(self) -> None:
#     pass
