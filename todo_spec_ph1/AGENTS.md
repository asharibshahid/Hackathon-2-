# AGENTS Constitution

Purpose: This repository is run using spec-driven development. All changes must be traceable to approved specs.

Operating Rules
- Read AGENTS.md and relevant specs before any implementation.
- Do not write or change code unless the spec explicitly covers the behavior.
- If anything is unclear or missing, propose a spec update first and wait for approval.
- Follow the sequence: Constitution/AGENTS + Specs -> Plan -> Tasks -> Implement.
- Keep changes small, modular, and test-friendly.
- Store tasks in memory only; no files or databases.
- Use Python 3.10+ and keep dependencies to the standard library unless specs say otherwise.
- Handle errors gracefully and keep CLI behavior consistent with the CLI spec.

Spec Traceability
- Every feature must map to a section in specs/phase1.
- When implementing, reference the exact spec section in code comments only if needed for clarity.
- Do not add features not present in the specs.

Documentation Requirements
- Keep README.md accurate with run instructions and example session.
- Maintain CLAUDE.md as a forwarder containing only: @AGENTS.md

Quality Bar
- Functions should be small and single-purpose.
- Validate input in the service layer; models should be simple data holders.
- Use clear, user-friendly messages in the CLI.

Change Policy
- If specs need changes, update specs first, then update the plan and task list, then implement.