# Architecture

Components
- Frontend: Next.js App Router in /frontend.
- Backend: FastAPI in /backend.
- Database: Neon Postgres accessed via SQLModel in the backend.

Request Flow
1. The user interacts with the frontend UI to manage tasks.
2. The frontend calls backend REST endpoints under /api.
3. The backend validates the JWT, enforces user isolation, and reads/writes tasks via SQLModel.
4. The backend returns JSON responses; the frontend updates the UI.

Cross-Origin Requests
- The backend enables CORS to allow browser requests from the frontend during development.
- Phase 2 allows all origins for simplicity.

JWT Flow
1. The user signs up or logs in via Better Auth on the frontend.
2. Better Auth issues a JWT to the frontend.
3. The frontend sends every API request with `Authorization: Bearer <token>`.
4. The backend verifies the JWT using a shared secret, extracts `user_id` from the `sub` claim, and compares it to the `{user_id}` path parameter.
5. Requests with missing/invalid tokens or mismatched user IDs are rejected.
