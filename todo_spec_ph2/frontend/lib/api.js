import { clearToken, getToken } from "./auth";

const DEFAULT_BASE_URL = "http://localhost:8000";

function getBaseUrl() {
  return process.env.BACKEND_URL || DEFAULT_BASE_URL;
}

function buildUrl(path) {
  if (!path.startsWith("/")) {
    return `${getBaseUrl()}/${path}`;
  }
  return `${getBaseUrl()}${path}`;
}

async function handleResponse(response) {
  if (response.status === 204) {
    return null;
  }
  const data = await response.json().catch(() => null);
  if (!response.ok) {
    const message = data?.detail || data?.error || "Request failed";
    const error = new Error(message);
    error.status = response.status;
    throw error;
  }
  return data;
}

export async function apiRequest(path, options = {}) {
  const token = getToken();
  if (!token) {
    throw new Error("Missing token");
  }

  const headers = new Headers(options.headers || {});
  headers.set("Authorization", `Bearer ${token}`);
  if (options.body && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const response = await fetch(buildUrl(path), {
    ...options,
    headers,
    cache: "no-store",
  });

  if (response.status === 401 || response.status === 403) {
    clearToken();
  }

  return handleResponse(response);
}

export async function authRequest(path, payload) {
  const response = await fetch(buildUrl(path), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
    cache: "no-store",
  });

  return handleResponse(response);
}
