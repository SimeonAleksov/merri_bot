from events.base_event import BaseEvent
from utils import get_channel
from datetime import datetime


class ExampleEvent(BaseEvent):

    def __init__(self):
        interval_minutes = 60
        super().__init__(interval_minutes)


    async def run(self, client):
        now = datetime.now()

        if now.hour == 12:
            msg = "It's high noon!"
        else:
            msg = f"It is {now.hour}:{now.minute}"

        channel = get_channel(client, "general")
        await client.send_message(channel, msg)
