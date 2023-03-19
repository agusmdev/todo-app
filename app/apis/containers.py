"""Module to provide the containers with injected services for the app"""

from dependency_injector import containers, providers

from app.apis.repositories import get_repository
from app.apis.task import routers as task_router
from app.apis.task.container import TaskContainer

from .config import settings


class AppContainer(containers.DeclarativeContainer):
    """Container to serve all the containers related to the app"""

    # Set wiring between endpoints and injected repositories
    wiring_config = containers.WiringConfiguration(modules=[task_router])
    # Set configuration for the app
    config = providers.Configuration()
    # Setup container for task services
    repository = providers.Singleton(get_repository, settings.REPOSITORY_NAME)

    task_container = providers.Container(
        TaskContainer,
        repository=repository,
        config=config,
    )
