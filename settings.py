import os

COMMAND_PREFIX = "$"

BOT_TOKEN = os.environ["TOKEN"]

NOW_PLAYING = COMMAND_PREFIX + "help"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

