from datetime import datetime

from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    note_id: int | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    action_items: list[ActionItemRead] = []

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None


class ActionItemCreate(BaseModel):
    description: str
    note_id: int | None = None


class ActionItemPatch(BaseModel):
    description: str | None = None
    completed: bool | None = None


class TagCreate(BaseModel):
    name: str


class TagRead(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NoteWithTagIds(BaseModel):
    tag_ids: list[int]
