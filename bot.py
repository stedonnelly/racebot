from iirl import bot

from iirl.team_handling import *
from iirl.attendance_window import *
from iirl.tasks import *
from iirl import refresh_tier_data, refresh_race_data
from iirl.config_manager import Config

import sys

config = Config.load()

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is ready and logged in as {bot.user}")

dev = sys.argv[1] if len(sys.argv) > 1 else False

# Run the bot
if dev == "dev":
    bot.run(config.bot_dev_key) # Dev bot token
elif dev == False:
    bot.run(config.bot_key)  # Replace with your bot token
else:
    raise ValueError("Invalid argument. Please use 'dev' to run the bot in development mode.")
