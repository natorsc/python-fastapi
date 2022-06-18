from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import poll as crud
from ..database import get_db
from ..schemas import poll as schemas
from ..settings import Settings, get_settings

settings: Settings = get_settings()

router = APIRouter(
    prefix='/v1/poll',
    tags=['polls'],
)


@router.get('/questions', response_model=list[schemas.ReadQuestions])
def read(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_questions(db, skip=skip, limit=limit)


@router.get('/questions/{pk}', response_model=schemas.ReadQuestions)
def detail(pk: str, db: Session = Depends(get_db)):
    return crud.detail_question(db=db, pk=pk)


@router.post('/questions')
def create(data: schemas.CreateQuestion, db: Session = Depends(get_db)):
    return crud.create_question(db=db, data=data)


@router.patch('/questions/{pk}')
def update(pk: str, data: schemas.UpdateQuestion, db: Session = Depends(get_db)):
    return crud.update_question(db=db, pk=pk, data=data)


@router.delete('/questions/{pk}')
def delete(pk: str, db: Session = Depends(get_db)):
    return crud.delete_question(db=db, pk=pk)


# @router.get('/questions/{choice_pk}/choices/{choice_pk}/votes', response_model=list[ChoiceVotes])
# def detail(pk, db: Session = Depends(get_db)):
#    return detail_data(pk, db)
