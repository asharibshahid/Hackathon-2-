# Data Model

Task
Fields
- id: int, auto-incrementing starting at 1
- title: str, required
- description: str, optional (empty string allowed)
- completed: bool, default False

Validation Rules
- Title must be non-empty after trimming whitespace.
- Description may be empty or omitted.
- id must reference an existing task for update, delete, or toggle operations.

Storage Rules
- Tasks are stored in memory only for the life of the program.