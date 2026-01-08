# Data Model: In-Memory Console Todo App

**Feature**: 001-todo-app-core
**Date**: 2026-01-05
**Source**: spec.md (Key Entities section)

## Entities

### Task

Represents a single todo item in the application.

| Field | Type | Constraints | Default | Description |
|-------|------|-------------|---------|-------------|
| id | int | Positive, unique, immutable | Auto-generated | Unique identifier for the task |
| title | str | 1-200 characters, required | None (required) | Brief description of the task |
| description | str \| None | 0-1000 characters, optional | None | Additional details about the task |
| completed | bool | - | False | Whether the task is done |

#### Validation Rules

1. **id**: Must be a positive integer. Auto-generated starting from 1, incrementing by 1 for each new task. Deleted IDs are NOT reused.

2. **title**:
   - Required (cannot be None or empty)
   - Must be 1-200 characters after stripping whitespace
   - Whitespace-only strings are treated as empty (invalid)
   - Unicode characters allowed

3. **description**:
   - Optional (can be None or empty string)
   - Maximum 1000 characters
   - Unicode characters allowed

4. **completed**:
   - Boolean only (True/False)
   - Defaults to False on creation

#### State Transitions

```
┌──────────┐                    ┌───────────┐
│  Pending │ ───── toggle ────▶ │ Completed │
│(completed│ ◀──── toggle ───── │(completed │
│ = False) │                    │ = True)   │
└──────────┘                    └───────────┘
```

The task can transition between Pending and Completed states via the toggle operation. This is the only state change supported.

## Storage Model

### In-Memory Store

| Component | Type | Purpose |
|-----------|------|---------|
| tasks | dict[int, Task] | Primary storage, keyed by task ID |
| next_id | int | Counter for ID generation, starts at 1 |

#### Operations

| Operation | Input | Output | Side Effects |
|-----------|-------|--------|--------------|
| add_task | title, description? | Task | Increments next_id, adds to tasks dict |
| list_tasks | - | list[Task] | None |
| get_task | id | Task \| None | None |
| update_task | id, title?, description? | Task \| None | Updates task in dict |
| delete_task | id | bool | Removes from dict if exists |
| toggle_complete | id | Task \| None | Flips completed flag |

#### Invariants

1. `next_id` is always greater than any existing task ID
2. All task IDs in `tasks` dict are positive integers
3. No two tasks share the same ID
4. Deleted IDs are never reused within a session

## Relationships

This is a single-entity model with no relationships. The Task entity is self-contained.

## Future Considerations (Out of Scope for Phase 1)

These fields/entities may be added in future phases:

- `created_at: datetime` - Timestamp of task creation
- `updated_at: datetime` - Timestamp of last modification
- `priority: int` - Task priority level
- `due_date: date` - Task deadline
- `tags: list[str]` - Categorization tags
- `Category` entity - For grouping tasks

These are documented for awareness but MUST NOT be implemented in Phase 1.
