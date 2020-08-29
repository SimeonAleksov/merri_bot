from commands.base_command import BaseCommand
from utils import get_emoji


class hey(BaseCommand):
    def __init__(self):
        description = "greetz"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = message.author.mention + f" hiii {get_emoji(':smirk:')}\n"

        await message.channel.send(msg)
