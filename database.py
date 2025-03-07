from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base


class Database:
    def __init__(self, async_mode=False):
        self.async_mode = async_mode
        self.engine = None
        self.Session = None

    def connect_sync(self):
        config = dotenv_values()
        DB_URL = f'postgresql://{config["DB_USER"]}:{config["DB_PASSWORD"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'

        self.engine = create_engine(DB_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    async def connect_async(self):
        config = dotenv_values()
        DB_URL = f'postgresql+asyncpg://{config["DB_USER"]}:{config["DB_PASSWORD"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'

        self.engine = create_async_engine(DB_URL, echo=True)
        self.Session = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def get_session(self):
        if self.Session is None:
            self.connect_sync()
        return self.Session()

    async def get_session_async(self):
        if self.Session is None:
            await self.connect_async()
        return self.Session()

    async def close(self):
        if self.engine:
            await self.engine.dispose() if self.async_mode else self.engine.dispose()
