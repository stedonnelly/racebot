# utils/discord.py
import requests
import os

DISCORD_BASE_URL = "https://discord.com/api/v10"
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

def get_guild_members(guild_id: str, limit: int = 1000):
    url = f"{DISCORD_BASE_URL}/guilds/{guild_id}/members?limit={limit}"
    headers = {
        "Authorization": BOT_TOKEN
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Discord API error: {response.status_code}")
    return response.json()
