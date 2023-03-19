"""Unit testing for app.apis.task.repositories"""

from redbird.repos import MemoryRepo

from app.apis.repositories import get_repository, str_to_class
from app.apis.task.models import TaskDB


def test_str_to_class():
    assert str_to_class("MemoryRepo") == MemoryRepo
    assert str_to_class("NotExistingClass") is None
    assert str_to_class("BaseModel") is None  # Only valid repositories


def test_get_repository():
    assert isinstance(
        get_repository("MemoryRepo", id_field="task_id", model=TaskDB),
        MemoryRepo,
    )
    assert get_repository("not_supported_db", "task_id", TaskDB) is None
