from dataclasses import dataclass
from typing import Optional

@dataclass
class ControllerResponse:
    succes: bool
    type: int
    msg: Optional[str]

@dataclass
class Command:
    name: str
    options: Optional[list[any]]


class CommandQueue():
    def __init__(self):
        self._queue: list[Command] = None
        self._len: int = -1

        self._MAX_CAPACITY = 10


    def get(self) -> Command:
        if self._len != -1:
            cmd = self._queue[self._len]
            self._len = self._len - 1
            return cmd
        
    def add(self, cmd: Command):
        if self._len == self._MAX_CAPACITY:
            self._queue[self._len] = cmd
        else:
            self._queue.append(cmd)
            self._len = self._len + 1