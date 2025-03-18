from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from models import Base


class Database:
    def __init__(self, async_mode=False):
        self.async_mode = async_mode
        self.engine = None
        self.Session = None

    def connect(self):
        config = dotenv_values(".env")
        url = f'postgresql://{config["DB_USER"]}:{config["DB_PASSWORD"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'

        self.engine = create_engine(url, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    async def connect_async(self):
        config = dotenv_values(".env")
        url = f'postgresql+asyncpg://{config["DB_USER"]}:{config["DB_PASSWORD"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'

        self.engine = create_async_engine(url, echo=True)
        self.Session = async_sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    def create_tables(self):
        if self.engine:
            Base.metadata.create_all(self.engine)

    async def create_tables_async(self):
        if self.engine:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

    def get_session(self):
        if self.engine is None:
            self.connect()
        return self.Session()

    async def get_session_async(self):
        if self.engine is None:
            await self.connect_async()
        return self.Session()

    async def close_async(self):
        if self.engine:
            await self.engine.dispose()
