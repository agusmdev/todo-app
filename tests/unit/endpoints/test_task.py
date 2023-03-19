"""Unit testing for app.apis.task.routers"""
# pylint: disable=redefined-outer-name

import pytest
import pytest_asyncio
from pydantic_factories import ModelFactory

from app.apis.task.models import TaskDB


class TaskDBFactory(ModelFactory):
    __model__ = TaskDB


mocked_tasks = TaskDBFactory.batch(10)


@pytest_asyncio.fixture(scope="module", autouse=True)
async def mocked_repo(app):
    repo = app.container.task_container.task_repository()
    _ = [repo.add(mocked_task) for mocked_task in mocked_tasks]
    return repo


@pytest.mark.asyncio
async def test_get_task_exists(client):
    for task in mocked_tasks:
        task_id = task.task_id
        response = await client.get(
            f"/tasks/{task_id}",
        )
        assert response.status_code == 200
        result = response.json()
        assert TaskDB(**result) == task


@pytest.mark.asyncio
async def test_get_task_not_exists(client):
    not_valid_task_id = "9132687213"
    response = await client.get(
        f"/tasks/{not_valid_task_id}",
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_all_tasks(client):
    response = await client.get("/tasks")
    assert response.status_code == 200
    all_tasks = [TaskDB(**task) for task in response.json()]
    assert sorted(mocked_tasks, key=lambda x: x.task_id) == sorted(
        all_tasks, key=lambda x: x.task_id
    )


@pytest.mark.asyncio
async def test_create_task(client, mocked_repo):
    for task in mocked_tasks:
        new_task = task.dict()
        new_task.pop("task_id")

        response = await client.post(
            "/tasks",
            json=new_task,
        )
        new_task_id = response.json()["task_id"]
        assert response.status_code == 201
        created_task = mocked_repo.filter_by(task_id=new_task_id).first()
        assert created_task is not None


@pytest.mark.asyncio
async def test_update_task(client, mocked_repo):
    for task in mocked_tasks:
        task_id = task.task_id

        response = await client.patch(
            f"/tasks/{task_id}",
            json={"task_id": task_id, "description": "new description"},
        )
        assert response.status_code == 202
        updated_task = mocked_repo.filter_by(task_id=task_id).first()
        assert updated_task.description == "new description"


@pytest.mark.asyncio
async def test_delete_task(client, mocked_repo):
    for task in mocked_tasks:
        task_id = task.task_id

        existing_task = mocked_repo.filter_by(task_id=task_id).first()
        assert existing_task is not None

        response = await client.delete(f"/tasks/{task_id}")
        assert response.status_code == 204

        removed_task = mocked_repo.filter_by(task_id=task_id).first()
        assert removed_task is None


@pytest.mark.asyncio
async def test_sanity_check(client):
    response = await client.get(
        "/sanity-check",
    )

    assert response.status_code == 200
    data = response.json()
    assert data == "FastAPI running!"
