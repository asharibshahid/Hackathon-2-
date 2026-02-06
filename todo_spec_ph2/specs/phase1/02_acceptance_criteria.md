# Acceptance Criteria

Add Task
- When the user selects Add Task, the app prompts for a title and optional description.
- If the title is empty or whitespace, the app shows an error and does not create a task.
- A valid task is stored with a unique id and completed status set to False.

View Task List
- The app displays all tasks in a readable list.
- Each row shows id, title, and completed status.
- If no tasks exist, the app shows a friendly empty-state message.

Update Task
- The user can update a task by providing an id.
- If the id does not exist, the app shows an error and makes no changes.
- The user can update title, description, or both.
- If a new title is provided and it is empty or whitespace, the app shows an error and does not update the task.

Delete Task
- The user can delete a task by providing an id.
- If the id does not exist, the app shows an error and makes no changes.
- Successful deletion removes the task from storage.

Mark Complete (Toggle)
- The user can toggle completion status by providing an id.
- If the id does not exist, the app shows an error and makes no changes.
- The completed status switches between True and False on each toggle.