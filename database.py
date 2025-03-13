from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


class Database:
    def __init__(self):
        self.engine = None
        self.Session = None

    def connect(self):
        config = dotenv_values()

        DB_USER = config.get("DB_USER")
        DB_PASSWORD = config.get("DB_PASSWORD")
        DB_HOST = config.get("DB_HOST")
        DB_PORT = config.get("DB_PORT")
        DB_NAME = config.get("DB_NAME")

        DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

        self.engine = create_engine(DB_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def get_session(self):
        if self.Session is None:
            self.connect()
        return self.Session()

    def close(self):
        if self.engine:
            self.engine.dispose()
