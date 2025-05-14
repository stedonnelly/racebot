# -*- coding: utf-8 -*-
# bot/events/__init__.py

def setup(bot):
    from .guild_events import setup as setup_guild_events
    from .bot_lifecycle import setup as setup_lifecycle

    setup_guild_events(bot)
    setup_lifecycle(bot)