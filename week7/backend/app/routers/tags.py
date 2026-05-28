from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Note, Tag
from ..schemas import NoteRead, NoteWithTagIds, TagCreate, TagRead

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=list[TagRead])
def list_tags(db: Session = Depends(get_db)) -> list[TagRead]:
    rows = db.execute(select(Tag)).scalars().all()
    return [TagRead.model_validate(row) for row in rows]


@router.post("/", response_model=TagRead, status_code=201)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)) -> TagRead:
    tag = Tag(name=payload.name)
    db.add(tag)
    db.flush()
    db.refresh(tag)
    return TagRead.model_validate(tag)


@router.post("/{note_id}/tags", response_model=NoteRead)
def add_tags_to_note(note_id: int, payload: NoteWithTagIds, db: Session = Depends(get_db)) -> NoteRead:
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    tags = db.query(Tag).filter(Tag.id.in_(payload.tag_ids)).all()
    if len(tags) != len(payload.tag_ids):
        raise HTTPException(status_code=404, detail="One or more tags not found")
    note.tags = list(set(note.tags) | set(tags))
    db.add(note)
    db.flush()
    db.refresh(note)
    return NoteRead.model_validate(note)
