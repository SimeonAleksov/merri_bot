from os.path import join
from os import remove

from discord import HTTPException
from emoji import emojize

import settings


def get_rel_path(rel_path):
    return join(settings.BASE_DIR, rel_path)


def get_emoji(emoji_name, fail_silently=False):
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" \
        else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji


def get_channel(client, value, attribute="name"):
    channel = next((c for c in client.get_all_channels()
                    if getattr(c, attribute).lower() == value.lower()), None)
    if not channel:
        raise ValueError("No such channel")
    return channel


async def send_in_channel(client, channel_name, *args):
    await client.send_message(get_channel(client, channel_name), *args)


async def try_upload_file(client, channel, file_path, content=None,
                          delete_after_send=False, retries=3):
    used_retries = 0
    sent_msg = None

    while not sent_msg and used_retries < retries:
        try:
            sent_msg = await client.send_file(channel, file_path,
                                              content=content)
        except HTTPException:
            used_retries += 1

    if delete_after_send:
        remove(file_path)

    if not sent_msg:
        await client.send_message(channel,
                                  "Oops, something happened. Please try again.")

    return sent_msg
