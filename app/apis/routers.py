"""Module for including all the app's routers"""
from fastapi import APIRouter

from app.apis.task.routers import get_task_router


def get_app_router():
    router = APIRouter()
    router.include_router(get_task_router(), prefix="/tasks", tags=["tasks"])

    return router
