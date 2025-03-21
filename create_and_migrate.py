from alembic.config import Config
from alembic import command
from database import Database


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def create_tables():
    db = Database()
    db.create_tables()


def main():
    run_migrations()
    create_tables()


if __name__ == "__main__":
    main()
