"""Module with the routers related to the task service"""
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, HTTPException, status

from .schemas import TaskCreate, TaskResponse, TaskUpdate
from .service import TaskService


@inject
def get_task_router(task_service: TaskService = Provide["task_container.task_service"]):
    router = APIRouter()

    @router.post(
        "",
        response_description="Add new task",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_task(
        task: TaskCreate = Body(...),
    ) -> TaskResponse:
        return await task_service.create_task(task)

    @router.get(
        "",
        response_description="Get all the created entities",
        status_code=status.HTTP_200_OK,
    )
    async def get_all_tasks() -> List[TaskResponse]:
        return await task_service.get_all_tasks()

    @router.get(
        "/{task_id}",
        response_description="Get a single task",
        status_code=status.HTTP_200_OK,
    )
    async def get_task(
        task_id: str,
    ) -> TaskResponse:
        task = await task_service.get_task(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task {task_id} not found",
            )

        return task

    @router.patch(
        "/{task_id}",
        response_description="Update task",
        status_code=status.HTTP_202_ACCEPTED,
    )
    async def update_task(task_id: str, task: TaskUpdate = Body(...)) -> None:
        await task_service.update_task(task_id, task)

    @router.delete(
        "/{task_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        response_description="Delete task",
    )
    async def delete_task(
        task_id: str,
    ) -> None:
        await task_service.delete_task(task_id)

    return router
