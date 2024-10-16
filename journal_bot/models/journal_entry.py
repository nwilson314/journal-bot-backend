from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Session


class JournalEntryBase(SQLModel):
    content: str


class JournalEntry(JournalEntryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class JournalEntryCreate(JournalEntryBase):
    pass


class JournalEntryUpdate(JournalEntryBase):
    pass


def create_entry(session: Session, entry: JournalEntryCreate):
    db_entry = JournalEntry.model_validate(entry)
    session.add(db_entry)
    session.commit()
    session.refresh(db_entry)
    return db_entry


