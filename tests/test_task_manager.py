import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

import pytest

from app.models.task import TaskCreate, TaskType
from app.services.task_manager import TaskManager


@pytest.mark.asyncio
async def test_create_and_get_task():
    manager = TaskManager()
    data = TaskCreate(task_type=TaskType.VIDEO_TRANSLATE, input_url="http://example.com")
    task = await manager.create_task(data)
    fetched = await manager.get_task(task.id)
    assert fetched is not None
    assert fetched.id == task.id
    assert fetched.task_type == data.task_type


@pytest.mark.asyncio
async def test_delete_task():
    manager = TaskManager()
    data = TaskCreate(task_type=TaskType.VIDEO_TRANSLATE, input_url="http://example.com")
    task = await manager.create_task(data)
    success = await manager.delete_task(task.id)
    assert success is True
    assert await manager.get_task(task.id) is None
