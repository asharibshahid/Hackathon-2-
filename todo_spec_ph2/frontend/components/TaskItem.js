"use client";

import { useState } from "react";

export default function TaskItem({ task, onDelete, onToggle, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || "");
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  const handleCancel = () => {
    setTitle(task.title);
    setDescription(task.description || "");
    setError("");
    setIsEditing(false);
  };

  const handleSave = async () => {
    const trimmed = title.trim();
    if (!trimmed) {
      setError("Title is required.");
      return;
    }
    setSaving(true);
    setError("");
    try {
      await onUpdate(task.id, { title: trimmed, description });
      setIsEditing(false);
    } catch (err) {
      setError(err.message || "Failed to update task.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="task-item">
      <div className="task-meta">
        <h3>{task.title}</h3>
        <span className={`badge ${task.completed ? "completed" : ""}`}>
          {task.completed ? "Completed" : "Open"}
        </span>
      </div>

      {!isEditing && (
        <>
          <p className="muted">{task.description || "No description"}</p>
          <div className="button-row">
            <button className="secondary" onClick={() => onToggle(task.id)}>
              Toggle complete
            </button>
            <button className="secondary" onClick={() => setIsEditing(true)}>
              Edit
            </button>
            <button className="danger" onClick={() => onDelete(task.id)}>
              Delete
            </button>
          </div>
        </>
      )}

      {isEditing && (
        <>
          <div className="form-group">
            <label>Title</label>
            <input value={title} onChange={(event) => setTitle(event.target.value)} />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea
              value={description}
              onChange={(event) => setDescription(event.target.value)}
            />
          </div>
          <div className="button-row">
            <button onClick={handleSave} disabled={saving}>
              {saving ? "Saving..." : "Save"}
            </button>
            <button className="secondary" onClick={handleCancel}>
              Cancel
            </button>
          </div>
          {error && <p className="error">{error}</p>}
        </>
      )}
    </div>
  );
}
