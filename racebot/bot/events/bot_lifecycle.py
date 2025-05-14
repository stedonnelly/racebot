# -*- coding: utf-8 -*-
# bot/events/bot_lifecycle.py

from nextcord.ext import commands

def setup(bot: commands.Bot):

    @bot.event
    async def on_ready():
        print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_disconnect():
        print("⚠️ Bot disconnected")

    @bot.event
    async def on_resumed():
        print("🔄 Bot resumed after interruption")