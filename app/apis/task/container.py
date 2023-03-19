"""Module to provide the containers with injected services for the app"""

from dependency_injector import containers, providers

from app.apis.task.models import TaskDB
from app.apis.task.service import TaskService


class TaskContainer(containers.DeclarativeContainer):
    """Container to serve the Task service with the configured repository"""

    # Configuration to use
    config = providers.Configuration()

    repository = providers.Dependency()
    # Configure repository to use
    task_repository = providers.Singleton(
        repository,
        model=TaskDB,
    )

    # Configure service with repository
    task_service = providers.Singleton(TaskService, task_repo=task_repository)
