from datetime import datetime, timezone

from sqlmodel import Session, select

from ..models.task import Task, TaskCreate, TaskUpdate


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _normalize_title(title: str) -> str:
    trimmed = title.strip()
    if not trimmed:
        raise ValueError("Title must be non-empty")
    return trimmed


def list_tasks(session: Session, user_id: str) -> list[Task]:
    statement = select(Task).where(Task.user_id == user_id)
    return list(session.exec(statement))


def get_task(session: Session, user_id: str, task_id: int) -> Task | None:
    statement = select(Task).where(Task.user_id == user_id, Task.id == task_id)
    return session.exec(statement).first()


def create_task(session: Session, user_id: str, data: TaskCreate) -> Task:
    if data.title is None:
        raise ValueError("Title is required")
    title = _normalize_title(data.title)
    description = data.description or ""
    now = utc_now()

    task = Task(
        user_id=user_id,
        title=title,
        description=description,
        completed=False,
        created_at=now,
        updated_at=now,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, user_id: str, task_id: int, data: TaskUpdate) -> Task | None:
    if data.title is None or data.description is None:
        raise ValueError("Title and description are required")

    task = get_task(session, user_id, task_id)
    if task is None:
        return None

    task.title = _normalize_title(data.title)
    task.description = data.description
    task.updated_at = utc_now()

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, user_id: str, task_id: int) -> bool:
    task = get_task(session, user_id, task_id)
    if task is None:
        return False

    session.delete(task)
    session.commit()
    return True


def toggle_complete(session: Session, user_id: str, task_id: int) -> Task | None:
    task = get_task(session, user_id, task_id)
    if task is None:
        return None

    task.completed = not task.completed
    task.updated_at = utc_now()

    session.add(task)
    session.commit()
    session.refresh(task)
    return task
