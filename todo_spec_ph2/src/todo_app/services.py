from __future__ import annotations

from typing import List, Optional

from .models import Task
from .storage import InMemoryTaskRepository


class ValidationError(ValueError):
    pass


class NotFoundError(LookupError):
    pass


class TaskService:
    def __init__(self, repository: InMemoryTaskRepository) -> None:
        self._repository = repository

    def add_task(self, title: str, description: Optional[str]) -> Task:
        normalized_title = self._normalize_title(title, required=True)
        normalized_description = "" if description is None else description
        return self._repository.add(normalized_title, normalized_description)

    def list_tasks(self) -> List[Task]:
        return self._repository.list_all()

    def update_task(
        self,
        task_id: int,
        title: Optional[str],
        description: Optional[str],
    ) -> Task:
        task = self._repository.get(task_id)
        if task is None:
            raise NotFoundError("Task not found.")

        normalized_title: Optional[str] = None
        if title is not None:
            normalized_title = self._normalize_title(title, required=True)

        normalized_description = description if description is not None else None

        updated = self._repository.update(
            task_id,
            title=normalized_title,
            description=normalized_description,
        )
        if updated is None:
            raise NotFoundError("Task not found.")
        return updated

    def delete_task(self, task_id: int) -> None:
        if not self._repository.delete(task_id):
            raise NotFoundError("Task not found.")

    def toggle_complete(self, task_id: int) -> Task:
        updated = self._repository.toggle(task_id)
        if updated is None:
            raise NotFoundError("Task not found.")
        return updated

    def _normalize_title(self, title: str, required: bool) -> str:
        normalized = title.strip()
        if required and normalized == "":
            raise ValidationError("Title cannot be empty.")
        return normalized