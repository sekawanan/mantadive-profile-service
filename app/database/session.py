# app/database/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Declarative base
Base = declarative_base()

# Create the async engine using aiomysql
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Set to False in production
)

# Create the async session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get DB session
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session