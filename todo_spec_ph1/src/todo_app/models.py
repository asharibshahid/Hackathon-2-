from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = False