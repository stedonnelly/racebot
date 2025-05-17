# -*- coding: utf-8 -*-
# main.py

import os
import sys
import nextcord
from nextcord.ext import commands
from migrations import apply_migrations
from racebot.bot.events import setup as setup_events

from dotenv import load_dotenv
load_dotenv('.env')  # Load environment variables from .env file

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append it to sys.path
if current_dir not in sys.path:
    sys.path.append(current_dir)

intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  # optional, for user join tracking

bot = commands.Bot(command_prefix="!", intents=intents)

setup_events(bot)
#setup_commands(bot)  # optional: only if you have commands ready

import subprocess

if __name__ == "__main__":
    #apply_migrations()
    print(os.getcwd())
    print(current_dir)
    print(os.path.isdir("alembic"))
    subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"], check=True)
    if os.getenv("DEV") == "True":
        print("Running in development mode")
        bot.run(os.getenv("DISCORD_DEV_TOKEN"))
        # Load development-specific commands or settings here
    else:
        bot.run(os.getenv("DISCORD_BOT_TOKEN"))
