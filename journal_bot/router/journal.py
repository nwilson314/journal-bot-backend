from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from journal_bot.db import get_session
from journal_bot.models.journal_entry import JournalEntry, JournalEntryCreate, JournalEntryUpdate, create_entry

router = APIRouter(
    prefix="/journal",
    tags=["journal"],
)


@router.post("/")
async def create_journal_entry(
    entry: JournalEntryCreate,
    session: Session = Depends(get_session)
):  
    db_entry = create_entry(session, entry)
    return db_entry

@router.get("/{id}")
async def get_journal_entries(id: int, session: Session = Depends(get_session)):
    entry = session.get(JournalEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@router.patch("/{id}")
def update_journal_entry(id: int, entry: JournalEntryUpdate, session: Session = Depends(get_session)):
    entry = session.get(JournalEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    for field, value in entry.model_dump(exclude_unset=True).items():
        setattr(entry, field, value)
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry

@router.delete("/{id}")
def delete_journal_entry(id: int, session: Session = Depends(get_session)):
    entry = session.get(JournalEntry, id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    session.delete(entry)
    session.commit()
    return {"message": "Entry deleted"}