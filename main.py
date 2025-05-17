# main.py

import os
import sys
import asyncio
import subprocess
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from racebot.bot.bot import bot, get_token
from racebot.api.routers import servers, teams, drivers
from racebot.db.db import engine

load_dotenv(".env")

# Setup FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(servers.router, prefix="/servers", tags=["servers"])
app.include_router(teams.router, prefix="/teams", tags=["teams"])
app.include_router(drivers.router, prefix="/drivers", tags=["drivers"])

@app.on_event("startup")
async def startup_event():
    from migrations import apply_migrations
    apply_migrations()

@app.get("/status")
def status():
    return {"bot": str(bot.user) if bot.user else None, "ok": True}

# Run bot + API together
async def start():
    subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"], check=True)
    token = get_token()

    api_config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    api_server = uvicorn.Server(api_config)

    await asyncio.gather(
        bot.start(token),
        api_server.serve()
    )

if __name__ == "__main__":
    asyncio.run(start())
