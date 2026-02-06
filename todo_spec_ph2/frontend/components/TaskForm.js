"use client";

import { useState } from "react";

export default function TaskForm({ onCreate }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const trimmed = title.trim();
    if (!trimmed) {
      setError("Title is required.");
      return;
    }
    setError("");
    setSubmitting(true);
    try {
      await onCreate({ title: trimmed, description });
      setTitle("");
      setDescription("");
    } catch (err) {
      setError(err.message || "Failed to add task.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <h2>Add a task</h2>
      <div className="form-group">
        <label htmlFor="new-title">Title</label>
        <input
          id="new-title"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Design homepage"
        />
      </div>
      <div className="form-group">
        <label htmlFor="new-description">Description</label>
        <textarea
          id="new-description"
          value={description}
          onChange={(event) => setDescription(event.target.value)}
          placeholder="Optional details"
        />
      </div>
      <div className="button-row">
        <button type="submit" disabled={submitting}>
          {submitting ? "Adding..." : "Add task"}
        </button>
      </div>
      {error && <p className="error">{error}</p>}
    </form>
  );
}
