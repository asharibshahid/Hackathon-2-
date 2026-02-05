# CLI Commands

Interface Style
Menu-based CLI with numeric choices. The menu is shown after each completed action until the user exits.

Menu
- 1) Add Task
- 2) View Task List
- 3) Update Task
- 4) Delete Task
- 5) Toggle Complete
- 0) Exit

Prompts and Inputs
- Add Task prompts: "Title:" and "Description (optional):"
- Update Task prompts: "Task ID to update:", "New title (leave blank to keep current):", "New description (leave blank to keep current):"
- Delete Task prompt: "Task ID to delete:"
- Toggle Complete prompt: "Task ID to toggle:"

Output Format
- Task list rows: "[id] title | Completed: True/False"
- Empty list message: "No tasks yet."

Example Session
- Menu displayed
- User enters 1
- App prompts for title and description
- App confirms creation and returns to menu
- User enters 2
- App prints task list rows
- User enters 0 to exit