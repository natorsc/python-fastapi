import datetime

import sqlalchemy as sa

from ..database import Base


class Question(Base):
    __tablename__ = "question"

    id = sa.Column(sa.Integer, index=True, primary_key=True)
    question_text = sa.Column(sa.String(256), nullable=False)
    created = sa.Column(
        sa.DateTime, default=datetime.datetime.now)
    updated = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    choices = sa.orm.relationship('Choice', back_populates='question')


class Choice(Base):
    __tablename__ = 'choice'

    id = sa.Column(sa.Integer, index=True, primary_key=True)
    choice_text = sa.Column(sa.String(256), nullable=False)
    votes = sa.Column(sa.Integer, default=0, nullable=False)
    created = sa.Column(
        sa.DateTime, default=datetime.datetime.now)
    updated = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    question_id = sa.Column(sa.Integer, sa.ForeignKey('question.id'))
    question = sa.orm.relationship(
        'Question',
        back_populates='choices',
        foreign_keys=[question_id],
    )
