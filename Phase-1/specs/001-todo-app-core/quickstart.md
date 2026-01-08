# Quickstart Guide: In-Memory Console Todo App

**Feature**: 001-todo-app-core
**Date**: 2026-01-05

## Prerequisites

- Python 3.11 or higher
- UV package manager

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Phase-1
   ```

2. Initialize UV project (if not already done):
   ```bash
   uv init
   ```

3. Sync dependencies:
   ```bash
   uv sync
   ```

## Running the Application

### Option 1: Direct Python execution
```bash
python main.py
```

### Option 2: Module execution
```bash
python -m main
```

### Option 3: Via UV
```bash
uv run python main.py
```

## Basic Usage

### 1. Add a Task

```
Enter your choice (1-6): 1
Enter task title: Buy groceries
Enter task description (press Enter to skip): Milk, eggs, bread

Task created successfully with ID: 1
```

### 2. List All Tasks

```
Enter your choice (1-6): 2

========================================
              YOUR TASKS
========================================
[1] ✗ Buy groceries
    Description: Milk, eggs, bread
========================================
Total: 1 tasks (0 completed, 1 pending)
```

### 3. Toggle Task Completion

```
Enter your choice (1-6): 5
Enter task ID to toggle: 1

Task 1 marked as complete.
```

### 4. Update a Task

```
Enter your choice (1-6): 3
Enter task ID to update: 1
Enter new title (press Enter to keep current): Buy groceries and snacks
Enter new description (press Enter to keep current):

Task 1 updated successfully.
```

### 5. Delete a Task

```
Enter your choice (1-6): 4
Enter task ID to delete: 1

Task 1 deleted successfully.
```

### 6. Exit the Application

```
Enter your choice (1-6): 6

Thank you for using Todo App. Goodbye!
```

## Feature Summary

| Feature | Menu Option | Description |
|---------|-------------|-------------|
| Add Task | 1 | Create a new task with title and optional description |
| List Tasks | 2 | View all tasks with status indicators |
| Update Task | 3 | Modify title/description of existing task |
| Delete Task | 4 | Remove a task permanently |
| Toggle Complete | 5 | Mark task as done/undone |
| Exit | 6 | Close the application |

## Status Indicators

- ✗ = Pending (not completed)
- ✓ = Completed

## Limitations (Phase 1)

- All data is stored in memory only
- Data is lost when the application exits
- Single user only
- No search or filtering
- No priorities or due dates

## Troubleshooting

### "Command not found: python"
Ensure Python 3.11+ is installed and in your PATH:
```bash
python3 --version
```

### "No module named 'main'"
Ensure you're in the project root directory:
```bash
cd /path/to/Phase-1
```

### UV not installed
Install UV following official instructions:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Next Steps

After completing Phase 1:
- Phase 2 will add file-based persistence
- Phase 3 will add database storage and advanced features
