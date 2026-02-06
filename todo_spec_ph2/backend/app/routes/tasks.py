from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from ..db.session import get_session
from ..middleware.auth import require_authenticated_user
from ..models.task import TaskCreate, TaskRead, TaskUpdate
from ..services import tasks as task_service

router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])


def _invalid_title_error(exc: ValueError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc) or "Invalid title",
    )


@router.get("", response_model=list[TaskRead])
def list_tasks(
    user_id: str,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    return task_service.list_tasks(session, auth_user_id)


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    payload: TaskCreate,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    try:
        return task_service.create_task(session, auth_user_id, payload)
    except ValueError as exc:
        raise _invalid_title_error(exc)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    task = task_service.get_task(session, auth_user_id, task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    user_id: str,
    task_id: int,
    payload: TaskUpdate,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    try:
        task = task_service.update_task(session, auth_user_id, task_id, payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    deleted = task_service.delete_task(session, auth_user_id, task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return None


@router.patch("/{task_id}/complete", response_model=TaskRead)
def toggle_complete(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    auth_user_id: str = Depends(require_authenticated_user),
):
    task = task_service.toggle_complete(session, auth_user_id, task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
