"""Module with schemas for transforming data from requests and responses"""

from app.core.model_factory import optional_model

from .models import Task, TaskDB


class TaskCreate(Task):
    ...


@optional_model
class TaskUpdate(Task):
    ...


class TaskResponse(TaskDB):
    ...
