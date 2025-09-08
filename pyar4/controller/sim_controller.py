from pyar4.controller.base_controller import BaseController

class SimController(BaseController):
    def __init__(self, _config: dict):
        super().__init__(_config)

        raise NotImplementedError("SimController not implemented")
    
    def _startup(self) -> None:
        raise NotImplementedError

    def _stop(self) -> None:
        raise NotImplementedError
    
    def _listen(self) -> dict:
        raise NotImplementedError 
    
    def _move_joint(self, idx: int, val: float) -> None:
        raise NotImplementedError
    
    def _execute_trajectory(self, angles: list[list[float]]) -> None:
        raise NotImplementedError
    
    def _save_position(self, name: str) -> None:
        raise NotImplementedError
    
    def _move_to_position(self, name: str) -> None:
        raise NotImplementedError
    
    