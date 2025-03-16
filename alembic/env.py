import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from alembic import context
from models import Base
from dotenv import dotenv_values
from sqlalchemy.ext.asyncio import create_async_engine

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    env_vars = dotenv_values(".env")
    db_url = env_vars.get("DATABASE_URL")

    if not db_url:
        raise ValueError("DATABASE_URL is not set in the .env file")

    config.set_main_option("sqlalchemy.url", db_url)

    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    env_vars = dotenv_values(".env")
    db_url = env_vars.get("DATABASE_URL")

    if not db_url:
        raise ValueError("DATABASE_URL is not set in the .env file")

    config.set_main_option("sqlalchemy.url", db_url)

    connectable = create_async_engine(
        db_url,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
