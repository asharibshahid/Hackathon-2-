# Phase 1 Overview

Goal
Build a Python 3.10+ console Todo app with in-memory storage. The app supports adding, viewing, updating, deleting, and toggling completion status for tasks.

Scope
- CLI-based, menu-driven interaction.
- In-memory storage only.
- Clear separation of models, storage, services, and CLI.

Non-Goals
- No persistence (files, databases).
- No authentication or multi-user features.
- No external dependencies beyond Python standard library.

Success Definition
The app meets all acceptance criteria in specs/phase1/02_acceptance_criteria.md and follows the CLI behavior in specs/phase1/03_cli_commands.md.