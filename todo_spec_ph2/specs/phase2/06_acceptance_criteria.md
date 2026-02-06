# Acceptance Criteria

Authentication and Security
- Any API request without an `Authorization: Bearer <token>` header returns 401.
- Any API request with an invalid JWT returns 401.
- If the token user_id does not match the `{user_id}` path parameter, the API returns 403 and performs no data access or changes.

Database Persistence
- Creating a task stores it in Neon Postgres and it remains available after a backend restart.

List Tasks
- GET /api/{user_id}/tasks returns a JSON array of tasks that belong only to that user.
- Tasks belonging to other users are not included in the response.

Create Task
- POST /api/{user_id}/tasks with a non-empty title returns 201 and a Task object.
- The created task has completed set to false and includes created_at and updated_at.
- If the title is empty or whitespace, the API returns 400 and creates no task.

Get Task By Id
- GET /api/{user_id}/tasks/{id} returns 200 and the Task object when it exists for that user.
- If the task does not exist for that user, the API returns 404.

Update Task
- PUT /api/{user_id}/tasks/{id} with valid title and description returns 200 and the updated Task object.
- updated_at changes on successful update.
- If the title is empty or whitespace, the API returns 400 and makes no changes.

Delete Task
- DELETE /api/{user_id}/tasks/{id} returns 204 and removes the task.
- A subsequent GET for the same id returns 404.

Complete Toggle
- PATCH /api/{user_id}/tasks/{id}/complete toggles completed and returns 200 with the updated Task object.
- updated_at changes on a successful toggle.

UI Pages
- /signup displays a sign-up form and routes to /dashboard after a successful sign-up.
- /login displays a login form and routes to /dashboard after a successful login.
- /dashboard requires authentication; unauthenticated users are redirected to /login.
- /dashboard shows a task list and controls to add, edit, delete, and complete tasks.
- After any task action, the UI reflects the latest server state.

Frontend Auth Storage
- After successful signup or login, the JWT is stored in `localStorage` under `auth_token`.
- /dashboard derives `user_id` from the JWT payload and uses it for API requests.

Cross-Origin
- Browser requests from the frontend to the backend succeed without CORS errors.

Local Auth (Fallback)
- POST /auth/signup with non-empty email and password returns 200 with a JWT and user_id.
- POST /auth/login with non-empty email and password returns 200 with a JWT and user_id.
- Missing or empty email/password returns 400.
