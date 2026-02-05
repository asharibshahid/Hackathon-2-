# Requirements

User Stories
- As a user, I can add a task with a required title and an optional description.
- As a user, I can view a list of all tasks showing id, title, and completion status.
- As a user, I can update a task's title and/or description by id.
- As a user, I can delete a task by id.
- As a user, I can toggle a task as complete or incomplete by id.

Functional Requirements
- Provide a consistent, menu-based CLI.
- Validate inputs and show clear error messages.
- IDs are auto-incrementing integers starting at 1.
- The list view is readable and includes id, title, completed status.
- Update allows changing title and/or description without altering other fields.

Non-Functional Requirements
- Python 3.10+ compatible.
- In-memory storage only.
- Modular architecture with separate layers for model, storage, services, and CLI.
- Functions should be small and test-friendly.