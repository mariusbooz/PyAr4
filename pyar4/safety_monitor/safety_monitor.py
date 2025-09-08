class SafetyMonitor():
    def __init__(self):
        self.emergency = False

        self.reason: str = None
        raise NotImplementedError

    def trigger_emergency(self, reason: str):
        self.emergency = True
        self.reason = reason

    def is_triggered(self):
        return self.emergency