from pyar4.logging.logger import FileLogger
from pyar4.controller.servo_controller import ServoController
from pyar4.controller.sim_controller import SimController


class Ar4:
    """
    Main class to controll the robotic arm, handles all the high level logic and
    distributes tasks to other classes.

    Attributes:
        _controller(Controller) : Controller to communicate with either a servo, simulation or custom backend.
        _logger(FileLogger) :
    """

    def __init__(self, controller: str, dir_name: str):
        self._logger = FileLogger(_dir_name=dir_name)
        self._logger.info("Logger was sucessfully setup.")

        if controller == "servo":
            self._controller = ServoController()
        elif controller == "sim":
            self._controller = SimController()
        else:
            raise ValueError(
                f"{controller} is not a possible controller choice. It must be either 'servo', 'sim' or a custom implementation."
            )
        raise NotImplementedError(("Ar4 not implemented"))

    # Startup
    def startup(self) -> None:
        raise NotImplementedError

    # Safety / Control
    def stop(self) -> None:
        raise NotImplementedError

    def shutdown(self) -> None:
        raise NotImplementedError

    def calibrate(self) -> None:
        raise NotImplementedError

    # Movement
    def move_to(
        self, x: float, y: float, z: float, orientation: list[float] = None
    ) -> None:
        raise NotImplementedError

    def move_joint(self, idx: int, val: float) -> None:
        raise NotImplementedError

    def set_joint_angles(self, angles: list[float]) -> None:
        raise NotImplementedError

    def set_home(self) -> None:
        raise NotImplementedError

    def home(self) -> None:
        raise NotImplementedError

    def save_position(self, name: str, *args) -> None:
        raise NotImplementedError

    def move_to_position(self, name: str) -> None:
        raise NotImplementedError

    # Motion Planning
    def execute_trajectory(self, angles: list[list[float]]) -> None:
        raise NotImplementedError

    # Gripper
    def open_gripper(self) -> None:
        raise NotImplementedError

    def close_gripper(self) -> None:
        raise NotImplementedError

    # State / Sensoring
    def get_joint_angles(self) -> list[float]:
        raise NotImplementedError

    def get_position(self) -> list[float]:
        raise NotImplementedError
