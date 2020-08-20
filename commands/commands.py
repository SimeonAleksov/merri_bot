from commands.base_command import BaseCommand


class Help(BaseCommand):
    def __init__(self):
        description = "help reeeeee"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        from message_handler import COMMAND_HANDLERS
        msg = message.author.mention + "\n"
        for cmd in sorted(COMMAND_HANDLERS.items()):
            msg += "\n" + cmd[1].description

        await message.channel.send(msg)
