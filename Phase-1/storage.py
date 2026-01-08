"""In-memory storage for the Todo application."""

from models import Task

# Module-level storage state
_tasks: dict[int, Task] = {}
_next_id: int = 1


def get_task(task_id: int) -> Task | None:
    """Retrieve a task by its ID.

    Args:
        task_id: The unique identifier of the task.

    Returns:
        The Task if found, None otherwise.
    """
    return _tasks.get(task_id)


def add_task(title: str, description: str | None = None) -> Task:
    """Create a new task with the given title and optional description.

    Args:
        title: Task title (1-200 characters, pre-validated).
        description: Optional task description (0-1000 characters).

    Returns:
        The newly created Task with auto-generated ID.
    """
    global _next_id
    task = Task(id=_next_id, title=title, description=description, completed=False)
    _tasks[_next_id] = task
    _next_id += 1
    return task


def list_tasks() -> list[Task]:
    """Retrieve all tasks from storage.

    Returns:
        List of all Task objects, may be empty.
    """
    return list(_tasks.values())


def toggle_complete(task_id: int) -> Task | None:
    """Toggle a task's completed status.

    Args:
        task_id: The unique identifier of the task to toggle.

    Returns:
        The updated Task if found, None if task doesn't exist.
    """
    task = _tasks.get(task_id)
    if task is None:
        return None
    task.completed = not task.completed
    return task


def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None
) -> Task | None:
    """Update a task's title and/or description.

    Args:
        task_id: The unique identifier of the task to update.
        title: New title (if provided, must be 1-200 chars).
        description: New description (if provided, 0-1000 chars).

    Returns:
        The updated Task if found, None if task doesn't exist.
    """
    task = _tasks.get(task_id)
    if task is None:
        return None
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    return task


def delete_task(task_id: int) -> bool:
    """Delete a task by its ID.

    Args:
        task_id: The unique identifier of the task to delete.

    Returns:
        True if task was deleted, False if task didn't exist.
    """
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False
