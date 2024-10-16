from sqlmodel import SQLModel, create_engine, Session
from journal_bot.config import settings

# Create the database engine
engine = create_engine(settings.database_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
