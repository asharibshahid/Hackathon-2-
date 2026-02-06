# API Endpoints

Auth
- All endpoints require `Authorization: Bearer <token>`.

Task JSON Shape
- id: int
- user_id: str
- title: str
- description: str
- completed: bool
- created_at: ISO 8601 UTC string
- updated_at: ISO 8601 UTC string

GET /api/{user_id}/tasks
- Response 200: JSON array of Task objects for the authenticated user.
- Errors: 401 (missing/invalid token), 403 (user_id mismatch).

POST /api/{user_id}/tasks
- Request body: {"title": "...", "description": "..."} (description optional).
- Response 201: Task object for the created task.
- Errors: 400 (invalid title), 401, 403.

GET /api/{user_id}/tasks/{id}
- Response 200: Task object.
- Errors: 401, 403, 404 (not found for that user).

PUT /api/{user_id}/tasks/{id}
- Request body: {"title": "...", "description": "..."} (both required; description may be empty).
- Response 200: Task object for the updated task.
- Errors: 400 (invalid title or missing fields), 401, 403, 404.

DELETE /api/{user_id}/tasks/{id}
- Response 204: no content.
- Errors: 401, 403, 404.

PATCH /api/{user_id}/tasks/{id}/complete
- Request body: none.
- Behavior: toggle completed status and update updated_at.
- Response 200: Task object with updated completed status.
- Errors: 401, 403, 404.

Local Auth (Fallback if Better Auth is not configured)
- These endpoints do not require Authorization headers.

POST /auth/signup
- Request body: {"email": "...", "password": "..."}.
- Response 200: {"token": "<jwt>", "user_id": "<email>"}.
- Errors: 400 (missing or empty email/password).

POST /auth/login
- Request body: {"email": "...", "password": "..."}.
- Response 200: {"token": "<jwt>", "user_id": "<email>"}.
- Errors: 400 (missing or empty email/password).
