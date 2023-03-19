"""Module with the models for the DB connection"""
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class Status(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class Task(BaseModel):
    title: str
    status: Status
    description: Optional[str]


class TaskDB(Task):
    __colname__ = "tasks"
    __id_field__ = "task_id"

    task_id: str = Field(default_factory=lambda: uuid4().hex)
