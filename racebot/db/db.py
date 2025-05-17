# -*- coding: utf-8 -*-
# db/db.py

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base

#DATABASE_URL = "sqlite+aiosqlite:///./bot.db"
from urllib.parse import quote_plus

password = quote_plus("+5PPa1eYOKe=RoYD@KMb8TlL")
DATABASE_URL = f"mysql+asyncmy://u20695_4nLI10OUgq:%2B5PPa1eYOKe%3DRoYD%40KMb8TlL@5.78.106.41:3306/s20695_Default_DB"

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
