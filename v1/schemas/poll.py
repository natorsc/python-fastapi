import datetime

from pydantic import BaseModel


class BaseQuestion(BaseModel):
    question_text: str


class CreateQuestion(BaseQuestion):
    pass


class ReadQuestions(BaseQuestion):
    id: int
    created: datetime.datetime
    updated: datetime.datetime
    choices: list

    class Config:
        orm_mode = True


class UpdateQuestion(BaseQuestion):
    pass

