"use client";

import TaskItem from "./TaskItem";

export default function TaskList({ tasks, onDelete, onToggle, onUpdate }) {
  if (!tasks.length) {
    return <p className="muted">No tasks yet.</p>;
  }

  return (
    <div className="task-grid">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onDelete={onDelete}
          onToggle={onToggle}
          onUpdate={onUpdate}
        />
      ))}
    </div>
  );
}
