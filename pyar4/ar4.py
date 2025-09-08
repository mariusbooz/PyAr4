from pyar4.logging.logger import Logger
from pyar4.controller.servo_controller import ServoController
from pyar4.controller.sim_controller import SimController
from pyar4.scheduler.command_scheduler import CommandScheduler
from pyar4.safety_monitor.safety_monitor import SafetyMonitor
from pyar4.utils.kinematics import *
from pyar4.utils import load_config

class Ar4():
    def __init__(self):
        self._config = load_config()
        backend = self._config['robot']['backend']

        self._logger = Logger(self._config.get("logging", {}))
        self._logger.info("Setup Logger")
        
        if backend == 'real':
            self._controller = ServoController(self._config.get("hardware", {}))
        elif backend == 'sim':
            self._controller = SimController(self._config.get("hardware", {}))
        else:
            raise ValueError(f"{backend} is not a possible choice for backend. It must be either 'real' or 'sim'.")
        
        self._scheduler = CommandScheduler()
        self._safetyMonitor = SafetyMonitor()

        raise NotImplementedError(("Ar4 not implemented"))
    
    #Startup
    def startup(self) -> None:
        raise NotImplementedError
    
    #Safety / Control
    def stop(self) -> None:
        raise NotImplementedError
    
    def shutdown(self) -> None:
        raise NotImplementedError
    
    def calibrate(self) -> None:
        raise NotImplementedError
    
    #Movement
    def move_to(self, x: float, y: float, z: float, orientation: list[float]=None) -> None:
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
    
    #Motion Planning
    def execute_trajectory(self, angles: list[list[float]]) -> None:
        raise NotImplementedError
    
    #Gripper
    def open_gripper(self) -> None:
        raise NotImplementedError
    
    def close_gripper(self) -> None:
        raise NotImplementedError
    
    #State / Sensoring
    def get_joint_angles(self) -> list[float]:
        raise NotImplementedError
    
    def get_position(self) -> tuple[float, float, float]:
        raise NotImplementedError
    