"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import TaskForm from "../../components/TaskForm";
import TaskList from "../../components/TaskList";
import { apiRequest } from "../../lib/api";
import { clearToken, getToken, getUserId } from "../../lib/auth";

export default function DashboardPage() {
  const router = useRouter();
  const [userId, setUserId] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = getToken();
    const identity = getUserId();
    if (!token || !identity) {
      clearToken();
      router.replace("/login");
      return;
    }
    setUserId(identity);
  }, [router]);

  const handleAuthError = (err) => {
    if (err && (err.status === 401 || err.status === 403)) {
      clearToken();
      router.replace("/login");
      return true;
    }
    return false;
  };

  const loadTasks = useCallback(async () => {
    if (!userId) return;
    setLoading(true);
    setError("");
    try {
      const data = await apiRequest(`/api/${userId}/tasks`);
      setTasks(data || []);
    } catch (err) {
      if (handleAuthError(err)) return;
      setError(err.message || "Failed to load tasks.");
    } finally {
      setLoading(false);
    }
  }, [userId]);

  useEffect(() => {
    loadTasks();
  }, [loadTasks]);

  const handleCreate = async (payload) => {
    try {
      await apiRequest(`/api/${userId}/tasks`, {
        method: "POST",
        body: JSON.stringify(payload),
      });
      await loadTasks();
    } catch (err) {
      if (handleAuthError(err)) return;
      throw err;
    }
  };

  const handleUpdate = async (taskId, payload) => {
    try {
      await apiRequest(`/api/${userId}/tasks/${taskId}`, {
        method: "PUT",
        body: JSON.stringify(payload),
      });
      await loadTasks();
    } catch (err) {
      if (handleAuthError(err)) return;
      throw err;
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await apiRequest(`/api/${userId}/tasks/${taskId}`, {
        method: "DELETE",
      });
      await loadTasks();
    } catch (err) {
      if (handleAuthError(err)) return;
      throw err;
    }
  };

  const handleToggle = async (taskId) => {
    try {
      await apiRequest(`/api/${userId}/tasks/${taskId}/complete`, {
        method: "PATCH",
      });
      await loadTasks();
    } catch (err) {
      if (handleAuthError(err)) return;
      throw err;
    }
  };

  const handleSignOut = () => {
    clearToken();
    router.replace("/login");
  };

  if (!userId) {
    return (
      <div className="container">
        <div className="card auth-card">
          <h1>Checking session...</h1>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="header">
        <div>
          <h1>Your tasks</h1>
          <p className="muted">Signed in as {userId}</p>
        </div>
        <button className="secondary" onClick={handleSignOut}>
          Sign out
        </button>
      </div>

      <div className="task-grid" style={{ marginBottom: "24px" }}>
        <TaskForm onCreate={handleCreate} />
      </div>

      <div className="card">
        <h2>Task list</h2>
        {loading ? (
          <p className="muted">Loading tasks...</p>
        ) : (
          <TaskList tasks={tasks} onDelete={handleDelete} onToggle={handleToggle} onUpdate={handleUpdate} />
        )}
        {error && <p className="error">{error}</p>}
      </div>
    </div>
  );
}
