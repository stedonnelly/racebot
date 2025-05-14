# -*- coding: utf-8 -*-
# main.py

import os
import nextcord
from nextcord.ext import commands
from racebot.migrations import apply_migrations
from racebot.bot.events import setup as setup_events

from dotenv import load_dotenv
load_dotenv('.env')  # Load environment variables from .env file
intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  # optional, for user join tracking

bot = commands.Bot(command_prefix="!", intents=intents)

setup_events(bot)
#setup_commands(bot)  # optional: only if you have commands ready

if __name__ == "__main__":
    apply_migrations()
    if os.getenv("DEV") == "True":
        print("Running in development mode")
        bot.run(os.getenv("DISCORD_DEV_TOKEN"))
        # Load development-specific commands or settings here
    else:
        bot.run(os.getenv("DISCORD_BOT_TOKEN"))
