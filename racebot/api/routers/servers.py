# racebot/api/routers/servers.py

from fastapi import APIRouter, HTTPException
from racebot.bot.bot import bot  # Access the running bot instance
from nextcord import Guild

router = APIRouter()

@router.get("/{guild_id}/members")
async def get_discord_guild_members(guild_id: int):
    guild: Guild = bot.get_guild(int(guild_id))
    if not guild:
        raise HTTPException(status_code=404, detail="Guild not found or not in cache")

    await guild.chunk()  # ensure member list is populated

    return [
        {
            "id": str(m.id),
            "username": m.name,
            "display_name": m.display_name,
        }
        for m in guild.members
    ]

@router.get("/ping")
def ping():
    return {"message": "Server router is active"}
