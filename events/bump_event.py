from events.base_event import BaseEvent
from utils import get_channel
from datetime import datetime


class BumpEvent(BaseEvent):

    def __init__(self):
        interval_minutes = 20
        super().__init__(interval_minutes)

    async def run(self, client):
        now = datetime.now()
        channel = client.get_channel(694686681533775972)
        await channel.send("drink water")
