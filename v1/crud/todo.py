from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models.todo import ToDo
from ..schemas.todo import TodoCreate, TodoUpdate

HTML_CODES = {
    404: 'Não foi possível localizar a tarefa id = {pk}.',
}


def create_task(db: Session, task: TodoCreate):
    new_task = ToDo(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def read_task(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ToDo).offset(skip).limit(limit).all()


def detail_task(pk: str, db: Session):
    query = db.query(ToDo).filter(ToDo.id == pk)
    if query.first():
        return query.first()
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES[404].format(pk=pk)
    )


def update_task(pk: str, db: Session, task: TodoUpdate):
    query = db.query(ToDo).filter(ToDo.id == pk)
    if query.first():
        query.update(dict(task))
        db.commit()
        return task
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES[404].format(pk=pk)
    )


def delete_task(pk: str, db: Session):
    query = db.query(ToDo).filter(ToDo.id == pk)
    if query.first():
        query.delete()
        db.commit()
        return {f'detail': 'Tarefa id = {pk} removida com sucesso.'}
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES[404].format(pk=pk)
    )
