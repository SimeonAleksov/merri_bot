class BaseEvent:

    def __init__(self, interval_minutes):
        self.interval_minutes = interval_minutes

    async def run(self, client):
        raise NotImplementedError
