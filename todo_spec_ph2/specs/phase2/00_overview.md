# Phase 2 Overview

Goal
Build a multi-user web app for managing tasks with persistent storage in Neon Postgres.

Scope
- Monorepo with /frontend (Next.js App Router) and /backend (FastAPI).
- REST API for tasks as defined in specs/phase2/03_api_endpoints.md.
- Authentication via Better Auth on the frontend with JWT verification on the backend.
- SQLModel for database access and persistence.

Non-Goals
- CLI interface or in-memory-only storage.
- Real-time collaboration or shared editing.
- Support for databases other than Postgres.

Success Definition
The system meets all acceptance criteria in specs/phase2/06_acceptance_criteria.md.
