# Database Schema

SQLModel is the ORM for Neon Postgres.

Task Table (tasks)
Fields
- id: int, primary key, auto-increment.
- user_id: str, required, indexed; must match the authenticated user's id.
- title: str, required, non-empty after trimming whitespace.
- description: str, optional, default empty string.
- completed: bool, default False.
- created_at: datetime, required; stored in UTC.
- updated_at: datetime, required; stored in UTC and updated on every write.

Validation Rules
- title must be non-empty after trimming whitespace.
- user_id is required and comes from the authenticated JWT.
- created_at and updated_at are set by the backend, not the client.
