import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    task: str
    done: bool


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: int
    created: datetime.datetime
    updated: datetime.datetime

    class Config:
        orm_mode = True


class TodoUpdate(TodoBase):
    pass
