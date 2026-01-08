# CLI Interface Contract

**Feature**: 001-todo-app-core
**Date**: 2026-01-05
**Module**: `cli.py`, `main.py`

## Overview

This document defines the user-facing CLI interface contract, including menu structure, input/output formats, and user experience specifications.

## Menu Structure

### Main Menu Display

```
========================================
         TODO APPLICATION
========================================

1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit

Enter your choice (1-6):
```

### Menu Option Mapping

| Option | Action | Handler |
|--------|--------|---------|
| 1 | Add Task | `handle_add_task()` |
| 2 | List Tasks | `handle_list_tasks()` |
| 3 | Update Task | `handle_update_task()` |
| 4 | Delete Task | `handle_delete_task()` |
| 5 | Toggle Complete | `handle_toggle_complete()` |
| 6 | Exit | Clean exit with message |

## Input/Output Specifications

### Add Task Flow

**Input Prompts**:
```
Enter task title: <user input>
Enter task description (press Enter to skip): <user input>
```

**Success Output**:
```
Task created successfully with ID: {id}
```

**Error Outputs**:
```
Error: Title cannot be empty.
Error: Title must be 200 characters or less.
Error: Description must be 1000 characters or less.
```

---

### List Tasks Flow

**Output (with tasks)**:
```
========================================
              YOUR TASKS
========================================
[1] ✗ Buy groceries
    Description: Milk, eggs, bread

[2] ✓ Finish report
    Description: Q4 sales report

[3] ✗ Call mom
    (No description)
========================================
Total: 3 tasks (1 completed, 2 pending)
```

**Output (no tasks)**:
```
========================================
              YOUR TASKS
========================================
No tasks yet. Add your first task!
========================================
```

---

### Update Task Flow

**Input Prompts**:
```
Enter task ID to update: <user input>
Enter new title (press Enter to keep current): <user input>
Enter new description (press Enter to keep current): <user input>
```

**Success Output**:
```
Task {id} updated successfully.
```

**Error Outputs**:
```
Error: Task with ID {id} not found.
Error: Please enter a valid task ID (positive number).
Error: Title cannot be empty.
Error: Title must be 200 characters or less.
Error: Description must be 1000 characters or less.
```

---

### Delete Task Flow

**Input Prompts**:
```
Enter task ID to delete: <user input>
```

**Success Output**:
```
Task {id} deleted successfully.
```

**Error Outputs**:
```
Error: Task with ID {id} not found.
Error: Please enter a valid task ID (positive number).
```

---

### Toggle Complete Flow

**Input Prompts**:
```
Enter task ID to toggle: <user input>
```

**Success Output**:
```
Task {id} marked as complete.
```
or
```
Task {id} marked as pending.
```

**Error Outputs**:
```
Error: Task with ID {id} not found.
Error: Please enter a valid task ID (positive number).
```

---

### Exit Flow

**Output**:
```
Thank you for using Todo App. Goodbye!
```

---

### Invalid Menu Choice

**Output**:
```
Error: Invalid choice. Please enter a number between 1 and 6.
```

## Input Validation Rules

### Title Validation
| Input | Result |
|-------|--------|
| Empty string | Error: Title cannot be empty |
| Whitespace only | Error: Title cannot be empty |
| 1-200 characters | Valid |
| >200 characters | Error: Title must be 200 characters or less |

### Description Validation
| Input | Result |
|-------|--------|
| Empty string / Enter | Valid (None) |
| 1-1000 characters | Valid |
| >1000 characters | Error: Description must be 1000 characters or less |

### ID Validation
| Input | Result |
|-------|--------|
| Positive integer | Valid |
| Zero | Error: Please enter a valid task ID |
| Negative | Error: Please enter a valid task ID |
| Non-numeric | Error: Please enter a valid task ID |
| Empty | Error: Please enter a valid task ID |

## Status Indicators

| Status | Symbol | Meaning |
|--------|--------|---------|
| Pending | ✗ | Task not completed |
| Complete | ✓ | Task completed |

## User Experience Guidelines

1. **Clear prompts**: Every input should have a clear prompt explaining what's expected
2. **Immediate feedback**: Success/error messages displayed immediately after action
3. **Error recovery**: After errors, user returns to appropriate prompt or menu
4. **Graceful exit**: Exit always works, displays farewell message
5. **Consistent formatting**: All outputs use consistent visual style
