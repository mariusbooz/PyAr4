class SerialInterface():
    def __init__(self):
        raise NotImplementedError
    
    async def read(self) -> str:
        raise NotImplementedError
    
    async def write(self, msg: str):
        raise NotImplementedError