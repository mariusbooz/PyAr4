from dataclasses import dataclass
from typing import Optional


@dataclass
class ControllerResponse:
    """
    Class to hold the response of a controller after an action

    Attributes:
        succes(bool): True, if the action was succesfull, False itherwise
        type(int): 0, if the action was succesfull, enumerates type of error
        msg(Optional[str]): Optional error-message to be displayed
    """

    succes: bool
    type: int
    msg: Optional[str]


@dataclass
class Command:
    name: str
    options: Optional[list[any]]
    raise NotImplementedError
