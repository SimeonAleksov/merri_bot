from commands.base_command import BaseCommand
import requests
import discord

class pfp(BaseCommand):
    def __init__(self):
        description = "shows pfp"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = f"{message.author.mention} \n"
        e = discord.Embed()
        e.set_image(url=message.author.avatar_url)
        await message.channel.send(msg, file=discord.File(message.author.avatar_url))
