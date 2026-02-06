"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { authRequest } from "../../lib/api";
import { setToken } from "../../lib/auth";

export default function SignupPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      const response = await authRequest("/auth/signup", { email, password });
      setToken(response.token);
      router.replace("/dashboard");
    } catch (err) {
      setError(err.message || "Signup failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card auth-card">
        <h1>Create account</h1>
        <p className="muted">Start managing your tasks in seconds.</p>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
            />
          </div>
          <div className="button-row">
            <button type="submit" disabled={loading}>
              {loading ? "Creating..." : "Sign up"}
            </button>
            <button
              type="button"
              className="secondary"
              onClick={() => router.push("/login")}
            >
              Back to login
            </button>
          </div>
          {error && <p className="error">{error}</p>}
        </form>
      </div>
    </div>
  );
}
