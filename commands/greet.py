from commands.base_command import BaseCommand


class hello(BaseCommand):
    def __init__(self):
        description = "greetz"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = message.author.mention + " hi UwU\n"

        await message.channel.send(msg)
