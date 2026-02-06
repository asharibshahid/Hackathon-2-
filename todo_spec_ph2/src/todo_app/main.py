from __future__ import annotations

from .cli import TodoCLI
from .services import TaskService
from .storage import InMemoryTaskRepository


def main() -> None:
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    cli = TodoCLI(service)
    cli.run()


if __name__ == "__main__":
    main()