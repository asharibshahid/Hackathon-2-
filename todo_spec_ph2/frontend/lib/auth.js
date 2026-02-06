const TOKEN_KEY = "auth_token";

function safeWindow() {
  return typeof window !== "undefined";
}

export function setToken(token) {
  if (!safeWindow()) return;
  window.localStorage.setItem(TOKEN_KEY, token);
}

export function getToken() {
  if (!safeWindow()) return null;
  return window.localStorage.getItem(TOKEN_KEY);
}

export function clearToken() {
  if (!safeWindow()) return;
  window.localStorage.removeItem(TOKEN_KEY);
}

function decodeBase64Url(segment) {
  try {
    const normalized = segment.replace(/-/g, "+").replace(/_/g, "/");
    const padded = normalized.padEnd(Math.ceil(normalized.length / 4) * 4, "=");
    const json = atob(padded);
    return JSON.parse(json);
  } catch {
    return null;
  }
}

export function decodeToken(token) {
  if (!token) return null;
  const parts = token.split(".");
  if (parts.length !== 3) return null;
  return decodeBase64Url(parts[1]);
}

export function getUserIdFromToken(token) {
  const payload = decodeToken(token);
  if (!payload) return null;
  return payload.sub || payload.email || null;
}

export function getUserId() {
  const token = getToken();
  return getUserIdFromToken(token);
}
