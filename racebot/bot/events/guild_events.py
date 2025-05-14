# -*- coding: utf-8 -*-
# bot/events/guild_events.py

from nextcord.ext import commands
from nextcord import Guild
from sqlalchemy import select
from ...db.db import AsyncSessionLocal
from ...models.server import Server

def setup(bot: commands.Bot):

    @bot.event
    async def on_guild_join(guild):
        async with AsyncSessionLocal() as session:
            exists = await session.scalar(
                select(Server).where(Server.discord_guild_id == str(guild.id))
            )
            if not exists:
                new_server = Server(discord_guild_id=str(guild.id), name=guild.name)
                session.add(new_server)
                await session.commit()
                print(f"[+] Joined new server: {guild.name} ({guild.id})")

    @bot.event
    async def on_guild_remove(guild):
        print(f"[-] Removed from server: {guild.name} ({guild.id})")
        # You could soft-delete or log here