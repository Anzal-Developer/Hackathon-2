"""Data models for the Todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo task item.

    Attributes:
        id: Unique positive integer identifier (auto-generated, immutable).
        title: Required text (1-200 characters) describing the task.
        description: Optional text (0-1000 characters) with additional details.
        completed: Boolean status indicating whether task is done (default: False).
    """

    id: int
    title: str
    description: str | None = None
    completed: bool = False
