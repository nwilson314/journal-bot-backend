from os import getcwd, path

from alembic.config import Config
from alembic import command
from sqlmodel import SQLModel, create_engine, Session

from journal_bot.settings import settings

# Create the database engine
engine = create_engine(settings.database_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)
    alembic_cfg = Config(path.join(getcwd(), "alembic.ini"))
    command.stamp(alembic_cfg, "head")


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    init_db()
