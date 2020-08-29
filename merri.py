import sys
import settings
import discord
import message_handler

from apscheduler.schedulers.asyncio import AsyncIOScheduler


this = sys.modules[__name__]
this.running = False

sched = AsyncIOScheduler()


def main():
    print("Starting up...")
    client = discord.Client()

    @client.event
    async def on_ready():
        if this.running:
            return

        this.running = True

        if settings.NOW_PLAYING:
            print("Setting NP game", flush=True)
            activity = discord.Game(name=f"{settings.NOW_PLAYING}")
            await client.change_presence(status=discord.Status.idle, activity=activity)
        print("Logged in!", flush=True)

    async def common_handle_message(message):
        text = message.content
        if text.startswith(settings.COMMAND_PREFIX) and text != settings.COMMAND_PREFIX:
            cmd_split = text[len(settings.COMMAND_PREFIX):].split()
            try:
                await message_handler.handle_command(cmd_split[0].lower(),
                                                     cmd_split[1:], message, client)
            except:
                print("Error while handling message", flush=True)
                raise

    @client.event
    async def on_message(message):
        await common_handle_message(message)

    @client.event
    async def on_message_edit(before, after):
        await common_handle_message(after)

    @client.event
    async def on_member_join(member):
        channel = client.get_channel(747429604528095323)
        rules_channel = client.get_channel(747431013281562705)
        role = discord.utils.get(member.guild.roles, name='NooPy')
        await member.add_roles(role)
        msg = f"Welcome {member.mention}, please check the {rules_channel.mention}."

        await channel.send(msg)
    client.run(settings.BOT_TOKEN)


if __name__ == "__main__":
    main()
