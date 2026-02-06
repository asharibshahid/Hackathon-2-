# Hackathon II: Evolution of Todo (Phase 1 + Phase 2)

## Phase 1 Overview
A Python 3.10+ console Todo app with in-memory storage. Supports adding, viewing, updating, deleting, and toggling completion for tasks.

### Phase 1 Features
- Add Task (title required, description optional)
- View Task List (id, title, completed status)
- Update Task (title/description by id)
- Delete Task (by id)
- Toggle Complete (by id)

### Phase 1 Constraints
- In-memory only (no files, no database)
- Standard library only
- Menu-based CLI

## Phase 2 Overview
A multi-user web app with a FastAPI backend and a Next.js App Router frontend. Tasks persist to Neon Postgres via SQLModel. JWT auth is required for all task APIs.

### Phase 2 Services
- Backend: `backend/app` (FastAPI)
- Frontend: `frontend` (Next.js App Router)

## Phase 2 Environment Variables
Backend (`backend/.env` or process env):
- `DATABASE_URL` (Neon Postgres connection string)
- `BETTER_AUTH_SECRET` (shared JWT secret)

Frontend (`frontend/.env.local`):
- `BACKEND_URL` (defaults to `http://localhost:8000`)

## How to Run (Phase 2)

### Backend
From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd backend
$env:DATABASE_URL = "<your_neon_url>"
$env:BETTER_AUTH_SECRET = "<your_secret>"
uvicorn app.main:app --reload
```

### Frontend
From the repository root:

```bash
cd frontend
npm install
# .env.local:
# BACKEND_URL=http://localhost:8000
npm run dev
```

## Phase 2 Manual Test Steps
1. Start backend and frontend.
2. Visit `http://localhost:3000/signup` and create an account.
3. Verify you are redirected to `/dashboard` and can add a task.
4. Edit the task and toggle completion.
5. Delete the task and confirm it is removed.
6. Refresh `/dashboard` to confirm tasks persist in the database.

## How to Run (Phase 1)
From the repository root in PowerShell:

```powershell
$env:PYTHONPATH = "${PWD}\src"; python -m todo_app.main
```

Or run from the `src` directory:

```bash
cd src
python -m todo_app.main
```

## Phase 1 Example Session
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

## Phase 1 Manual Test Script
1. Run: `python -m todo_app.main`
2. Choose `2` to view list. Expect: `No tasks yet.`
3. Choose `1` and enter title `Test task`, description `alpha`. Expect: created with id `1`.
4. Choose `2`. Expect: `[1] Test task | Completed: False`.
5. Choose `5`, enter `1`. Expect: completion toggled to `True`.
6. Choose `3`, enter `1`, set new title `Updated task`, leave description blank. Expect: `Task updated.` and description unchanged.
7. Choose `4`, enter `1`. Expect: `Task deleted.`
8. Choose `2`. Expect: `No tasks yet.`
9. Enter `0` to exit.
