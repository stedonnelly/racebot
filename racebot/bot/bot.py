# racebot/bot/bot.py
import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

from .events import setup as setup_events  # load your events

load_dotenv(".env")

intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Register events/commands
setup_events(bot)

def get_token():
    return (
        os.getenv("DISCORD_DEV_TOKEN")
        if os.getenv("DEV") == "True"
        else os.getenv("DISCORD_BOT_TOKEN")
    )
