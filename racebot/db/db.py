# -*- coding: utf-8 -*-
# db/db.py

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./bot.db"

# Async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Base for models
Base = declarative_base()

# Dependency-style usage (if needed):
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
