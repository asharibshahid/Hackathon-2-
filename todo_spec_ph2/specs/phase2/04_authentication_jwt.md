# Authentication and JWT

Frontend
- Better Auth handles sign-up and login and issues JWTs to the client.
- The frontend must send `Authorization: Bearer <token>` with every API request.
- The frontend stores the JWT in `localStorage` under the key `auth_token`.
- The frontend derives `user_id` by decoding the JWT payload and reading `sub` (fallback to `email`).
- If Better Auth is not configured, the frontend uses the local auth endpoints in specs/phase2/03_api_endpoints.md and stores the returned token in the same way.

Backend
- The backend verifies JWT signatures using a shared secret configured in both systems.
- The shared secret is provided via the `BETTER_AUTH_SECRET` environment variable.
- JWTs must use the `HS256` algorithm.
- The backend extracts user_id from the JWT `sub` claim; if `sub` is missing, fall back to the `email` claim.
- The backend compares the token user_id to the `{user_id}` path parameter and rejects mismatches.
- Missing or invalid tokens return 401.

JWT Claims
- sub: required; the canonical `user_id` string.
- email: optional; may be used as a fallback user_id.
- iat: optional; issued-at timestamp.
- exp: optional; expiration timestamp. Phase 2 does not enforce exp validation.

User Isolation
- A user can only read, create, update, or delete tasks where task.user_id equals the token user_id.
- Requests for another user's resources must return 403 without leaking data.
