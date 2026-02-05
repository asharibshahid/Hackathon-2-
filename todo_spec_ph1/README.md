# Hackathon II: Evolution of Todo (Phase 1)

## Overview
A Python 3.10+ console Todo app with in-memory storage. Supports adding, viewing, updating, deleting, and toggling completion for tasks.

## Features
- Add Task (title required, description optional)
- View Task List (id, title, completed status)
- Update Task (title/description by id)
- Delete Task (by id)
- Toggle Complete (by id)

## Constraints
- In-memory only (no files, no database)
- Standard library only
- Menu-based CLI

## How to Run
From the repository root in PowerShell:

```powershell
$env:PYTHONPATH = "${PWD}\src"; python -m todo_app.main
```

Or run from the `src` directory:

```bash
cd src
python -m todo_app.main
```

## Example Session
```
Menu
1) Add Task
2) View Task List
3) Update Task
4) Delete Task
5) Toggle Complete
0) Exit
Select an option: 1
Title:Buy milk
Description (optional):2 liters
Task created with id 1.

Menu
1) Add Task
2) View Task List
3) Update Task
4) Delete Task
5) Toggle Complete
0) Exit
Select an option: 2
[1] Buy milk | Completed: False
```

## Manual Test Script
1. Run: `python -m todo_app.main`
2. Choose `2` to view list. Expect: `No tasks yet.`
3. Choose `1` and enter title `Test task`, description `alpha`. Expect: created with id `1`.
4. Choose `2`. Expect: `[1] Test task | Completed: False`.
5. Choose `5`, enter `1`. Expect: completion toggled to `True`.
6. Choose `3`, enter `1`, set new title `Updated task`, leave description blank. Expect: `Task updated.` and description unchanged.
7. Choose `4`, enter `1`. Expect: `Task deleted.`
8. Choose `2`. Expect: `No tasks yet.`
9. Enter `0` to exit.
