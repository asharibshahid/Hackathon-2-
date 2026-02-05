from __future__ import annotations

from typing import Dict, List, Optional

from .models import Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, title: str, description: str) -> Task:
        task = Task(id=self._next_id, title=title, description=description, completed=False)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list_all(self) -> List[Task]:
        return [self._tasks[task_id] for task_id in sorted(self._tasks.keys())]

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None

    def toggle(self, task_id: int) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.completed = not task.completed
        return task