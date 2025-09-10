from pyar4.utils.dataclasses import Command


class CommandQueue:
    """
    Queue for commands to a servo controller. Works on a first in - first out basis.

    Attributes:
        _queue(list[Command]) : List containing the commands currently in queue.
        _index(int) : Used to index the list of commands, is equal to the length of the queue - 1.
        __MAX_CAPACITY(int) : maximum capacity of the command queue, can be specified
    """

    def __init__(self, MAX_CAPACITY: int = 10):
        self._queue: list[Command] = None
        self._index: int = -1

        self.__MAX_CAPACITY: int = MAX_CAPACITY
        raise NotImplementedError

    def get(self) -> Command:
        """
        Returns the element at the front of the queue.
        """
        raise NotImplementedError

    def add(self, cmd: Command):
        """
        Add given command to the back of the queue, if MAX_CAPACITY is reached overrides earlier comamnds,
        behaviour can not be guaranteed.

        Parameters:
            cmd(Command) : Command object to be added to the queue.
        """
        raise NotImplementedError


class CommandScheduler:
    def __init__(self):
        raise NotImplementedError
