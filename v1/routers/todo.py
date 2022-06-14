from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud.todo import (create_task, delete_task, detail_task, read_task,
                         update_task)
from ..database import get_db
from ..schemas.todo import TodoCreate, TodoRead, TodoUpdate
from ..settings import Settings, get_settings

settings: Settings = get_settings()


router = APIRouter(
    prefix='/v1',
    tags=['todos'],
)


@router.get('/todos', response_model=list[TodoRead])
def read(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_task(db, skip=skip, limit=limit)


@router.get('/todos/{pk}', response_model=list[TodoRead])
def detail(pk, db: Session = Depends(get_db)):
    return detail_task(pk, db)


@router.post('/todos')
def create(task: TodoCreate, db: Session = Depends(get_db)):
    return create_task(task=task, db=db)


@router.patch('/todos/{pk}')
def update(pk: str, task: TodoUpdate, db: Session = Depends(get_db)):
    return update_task(pk=pk, task=task, db=db)


@router.delete('/todos/{pk}')
def delete(pk: str, db: Session = Depends(get_db)):
    return delete_task(pk=pk, db=db)
