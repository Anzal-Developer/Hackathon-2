# Storage API Contract

**Feature**: 001-todo-app-core
**Date**: 2026-01-05
**Module**: `storage.py`

## Overview

This document defines the internal API contract for the storage module. Since this is a CLI application (not a web API), these contracts define function signatures and behavior rather than HTTP endpoints.

## Function Contracts

### add_task

Creates a new task with auto-generated ID.

```python
def add_task(title: str, description: str | None = None) -> Task:
    """
    Create a new task with the given title and optional description.

    Args:
        title: Task title (1-200 characters, pre-validated)
        description: Optional task description (0-1000 characters)

    Returns:
        The newly created Task with auto-generated ID

    Raises:
        None - Validation happens at CLI layer
    """
```

**Preconditions**:
- `title` is non-empty and 1-200 characters (validated by caller)
- `description` is None or 0-1000 characters (validated by caller)

**Postconditions**:
- New Task exists in storage with unique ID
- Task.completed is False
- Internal ID counter is incremented

---

### list_tasks

Returns all tasks in the store.

```python
def list_tasks() -> list[Task]:
    """
    Retrieve all tasks from storage.

    Returns:
        List of all Task objects, may be empty
    """
```

**Preconditions**: None

**Postconditions**:
- Returns all tasks currently in storage
- Does not modify storage state
- Returns empty list if no tasks exist

---

### get_task

Retrieves a single task by ID.

```python
def get_task(task_id: int) -> Task | None:
    """
    Retrieve a task by its ID.

    Args:
        task_id: The unique identifier of the task

    Returns:
        The Task if found, None otherwise
    """
```

**Preconditions**:
- `task_id` is a positive integer

**Postconditions**:
- Returns Task if ID exists, None otherwise
- Does not modify storage state

---

### update_task

Updates an existing task's title and/or description.

```python
def update_task(
    task_id: int,
    title: str | None = None,
    description: str | None = None
) -> Task | None:
    """
    Update a task's title and/or description.

    Args:
        task_id: The unique identifier of the task to update
        title: New title (if provided, must be 1-200 chars)
        description: New description (if provided, 0-1000 chars)

    Returns:
        The updated Task if found, None if task doesn't exist
    """
```

**Preconditions**:
- `task_id` is a positive integer
- If `title` provided, it's 1-200 characters (validated by caller)
- If `description` provided, it's 0-1000 characters (validated by caller)

**Postconditions**:
- If task exists: fields are updated, returns updated Task
- If task doesn't exist: returns None, no state change
- Fields not provided remain unchanged

---

### delete_task

Removes a task from storage.

```python
def delete_task(task_id: int) -> bool:
    """
    Delete a task by its ID.

    Args:
        task_id: The unique identifier of the task to delete

    Returns:
        True if task was deleted, False if task didn't exist
    """
```

**Preconditions**:
- `task_id` is a positive integer

**Postconditions**:
- If task existed: removed from storage, returns True
- If task didn't exist: returns False, no state change
- Deleted ID is NOT reused

---

### toggle_complete

Toggles a task's completion status.

```python
def toggle_complete(task_id: int) -> Task | None:
    """
    Toggle a task's completed status.

    Args:
        task_id: The unique identifier of the task to toggle

    Returns:
        The updated Task if found, None if task doesn't exist
    """
```

**Preconditions**:
- `task_id` is a positive integer

**Postconditions**:
- If task exists: `completed` flipped (True↔False), returns updated Task
- If task doesn't exist: returns None, no state change

## Error Handling

The storage module does NOT raise exceptions for expected conditions (task not found). Instead:

| Condition | Return Value |
|-----------|--------------|
| Task not found | `None` or `False` |
| Task found | `Task` object or `True` |

This allows the CLI layer to handle user messaging appropriately.

## Thread Safety

Not required for Phase 1 (single-user, single-threaded application).
