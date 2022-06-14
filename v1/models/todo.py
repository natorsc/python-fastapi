import datetime

import sqlalchemy as sa

from ..database import Base


class ToDo(Base):
    __tablename__ = 'todos'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    task = sa.Column(sa.String(160), default='Nova tarefa.')
    done = sa.Column(sa.Boolean, default=True)
    created = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated = sa.Column(
        sa.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
