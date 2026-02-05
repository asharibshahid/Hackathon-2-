from __future__ import annotations

from typing import Optional

from .services import NotFoundError, TaskService, ValidationError


class TodoCLI:
    def __init__(self, service: TaskService) -> None:
        self._service = service

    def run(self) -> None:
        while True:
            self._print_menu()
            choice = input("Select an option: ").strip()
            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._update_task()
            elif choice == "4":
                self._delete_task()
            elif choice == "5":
                self._toggle_complete()
            elif choice == "0":
                print("Goodbye.")
                return
            else:
                print("Invalid option. Please try again.")

    def _add_task(self) -> None:
        title = input("Title:")
        description = input("Description (optional):")
        try:
            task = self._service.add_task(title, description)
        except ValidationError as exc:
            print(f"Error: {exc}")
            return
        print(f"Task created with id {task.id}.")

    def _view_tasks(self) -> None:
        tasks = self._service.list_tasks()
        if not tasks:
            print("No tasks yet.")
            return
        for task in tasks:
            print(f"[{task.id}] {task.title} | Completed: {task.completed}")

    def _update_task(self) -> None:
        task_id = self._prompt_for_id("Task ID to update:")
        if task_id is None:
            return
        raw_title = input("New title (leave blank to keep current):")
        raw_description = input("New description (leave blank to keep current):")

        title: Optional[str] = None if raw_title == "" else raw_title
        description: Optional[str] = None if raw_description == "" else raw_description

        try:
            self._service.update_task(task_id, title=title, description=description)
        except (ValidationError, NotFoundError) as exc:
            print(f"Error: {exc}")
            return
        print("Task updated.")

    def _delete_task(self) -> None:
        task_id = self._prompt_for_id("Task ID to delete:")
        if task_id is None:
            return
        try:
            self._service.delete_task(task_id)
        except NotFoundError as exc:
            print(f"Error: {exc}")
            return
        print("Task deleted.")

    def _toggle_complete(self) -> None:
        task_id = self._prompt_for_id("Task ID to toggle:")
        if task_id is None:
            return
        try:
            task = self._service.toggle_complete(task_id)
        except NotFoundError as exc:
            print(f"Error: {exc}")
            return
        print(f"Task {task.id} completed set to {task.completed}.")

    def _prompt_for_id(self, prompt: str) -> Optional[int]:
        raw = input(prompt)
        try:
            task_id = int(raw)
        except ValueError:
            print("Error: Invalid task id.")
            return None
        if task_id <= 0:
            print("Error: Invalid task id.")
            return None
        return task_id

    def _print_menu(self) -> None:
        print("\nMenu")
        print("1) Add Task")
        print("2) View Task List")
        print("3) Update Task")
        print("4) Delete Task")
        print("5) Toggle Complete")
        print("0) Exit")