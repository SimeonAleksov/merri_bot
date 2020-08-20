import settings
from commands.base_command import BaseCommand


COMMAND_HANDLERS = {c.__name__.lower(): c() for c in BaseCommand.__subclasses__()}


async def handle_command(command, args, message, bot_client):
    if command not in COMMAND_HANDLERS:
        print('NOPPPP')
        return

    print(f"{message.author.name}: {settings.COMMAND_PREFIX}{command} "
          + " ".join(args))

    cmd_obj = COMMAND_HANDLERS[command]
    if cmd_obj.params and len(args) < len(cmd_obj.params):
        await message.channel.send(message.author.mention + " Insufficient parameters!")
    else:
        await cmd_obj.handle(args, message, bot_client)
