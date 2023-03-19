"""Module with the Task service to serve"""
from typing import List, Optional

from redbird.templates import TemplateRepo

from .models import Task, TaskDB
from .schemas import TaskUpdate


class TaskService:
    """Service to interact with task collection.

    Args:
        task_repo (TemplateRepo): Repository for the DB connection
    """

    def __init__(self, task_repo: TemplateRepo) -> None:
        self.task_repo = task_repo

    async def get_task(self, task_id: str) -> Optional[TaskDB]:
        return self.task_repo.filter_by(task_id=task_id).first()

    async def get_all_tasks(self) -> List[TaskDB]:
        return self.task_repo.filter_by().all()

    async def create_task(self, task: Task) -> TaskDB:
        new_task = TaskDB(**task.dict())
        self.task_repo.add(new_task)
        return new_task

    async def update_task(self, task_id: str, updated_task: TaskUpdate) -> None:
        self.task_repo.filter_by(task_id=task_id).update(**updated_task.dict(exclude_unset=True))

    async def delete_task(self, task_id: str) -> None:
        self.task_repo.filter_by(task_id=task_id).delete()
