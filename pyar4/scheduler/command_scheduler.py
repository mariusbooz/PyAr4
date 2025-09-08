from pyar4.utils.dataclasses import *

class CommandScheduler:
    def __init__(self, controller, safety_monitor, logger):
        self.queue = CommandQueue()
        self.controller = controller
        self.safety = safety_monitor
        self.logger = logger
        raise NotImplementedError

    async def start_loop(self):
        while True:
            cmd = await self.queue.get()

            if self.safety.is_triggered():
                self.logger.log("Aborting: Emergency triggered")
                break

            result = await self.controller.execute(cmd)
            if not result.success:
                self.logger.log(f"Command failed: {result.message}")
                self.safety.trigger_emergency("Command failure")
                break