# UI Pages and Components

Routes
- /signup: Better Auth sign-up form (email + password) and submit action.
- /login: Better Auth login form (email + password) and submit action.
- /dashboard: authenticated task dashboard with list and task actions.

Core Components
- TaskList: renders the current user's tasks.
- TaskItem: shows title, description, completed status, and action buttons.
- TaskForm: used for adding a new task and editing an existing task.

Dashboard Behavior
- On load, fetch tasks via GET /api/{user_id}/tasks with the Authorization header.
- Add task uses POST /api/{user_id}/tasks.
- Edit task uses PUT /api/{user_id}/tasks/{id}.
- Delete task uses DELETE /api/{user_id}/tasks/{id}.
- Complete toggle uses PATCH /api/{user_id}/tasks/{id}/complete.
- After each action, refresh the list to reflect the latest server state.

Auth Flow and Storage
- If Better Auth is configured, /signup and /login use it to obtain a JWT.
- If Better Auth is not configured, /signup and /login call the local auth endpoints in specs/phase2/03_api_endpoints.md.
- Store the JWT in `localStorage` under `auth_token`.
- Derive `user_id` by decoding the JWT payload and reading `sub` (fallback to `email`).
- /dashboard redirects to /login when no valid token is present.

API Base URL
- The frontend uses the `BACKEND_URL` environment variable as the API base.
- If `BACKEND_URL` is not set, default to `http://localhost:8000`.
