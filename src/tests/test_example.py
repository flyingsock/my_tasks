import pytest
from src.task_manager import TaskManager


def test_add_task():
    t = TaskManager()
    t.add_task('hello')
    assert t.get_tasks == ['hello']
