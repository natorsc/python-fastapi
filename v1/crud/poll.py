from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models.poll import Choice, Question
from ..schemas import poll as schemas

HTML_CODES = {
    '404-question': 'Não foi possível localizar a questão id = {pk}.',
}


def create_question(db: Session, data: schemas.CreateQuestion):
    new_data = Question(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def read_questions(db: Session, limit: int = 100, skip: int = 0):
    return db.query(Question).offset(skip).limit(limit).all()


def detail_question(db: Session, pk: str):
    query = db.query(Question).filter(Question.id == pk)
    if query.first():
        return query.first()
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES['404-question'].format(pk=pk)
    )


def update_question(db: Session, data: schemas.CreateQuestion, pk: str):
    query = db.query(Question).filter(Question.id == pk)
    if query.first():
        query.update(dict(data))
        db.commit()
        return data
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES['404-question'].format(pk=pk)
    )


def delete_question(db: Session, pk: str):
    query = db.query(Question).filter(Question.id == pk)
    if query.first():
        query.delete()
        db.commit()
        return {f'detail': 'Tarefa id = {pk} removida com sucesso.'}
    raise HTTPException(
        status_code=404,
        detail=HTML_CODES[404].format(pk=pk)
    )
