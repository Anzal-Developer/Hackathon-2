# Implementation Plan: In-Memory Console Todo App

**Branch**: `001-todo-app-core` | **Date**: 2026-01-05 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-app-core/spec.md`

## Summary

Build a command-line Todo application with in-memory storage that supports CRUD operations (Add, List, Update, Delete, Toggle) through an interactive menu interface. The application follows clean architecture principles with separate modules for models, storage, and CLI handling. Uses Python 3.11+ with dataclasses for the Task entity and a dictionary-based in-memory store.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory dictionary (no persistence)
**Testing**: Manual testing (no test framework for Phase 1)
**Target Platform**: Cross-platform console (Linux/macOS/Windows)
**Project Type**: Single project
**Package Manager**: UV
**Performance Goals**: Menu displays < 1 second, all operations instant
**Constraints**: No external dependencies, no file I/O, no database
**Scale/Scope**: Single user, single session, ~100 tasks maximum expected

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-First Development | PASS | spec.md created and approved before plan |
| II. Simplicity Over Cleverness | PASS | Flat module structure, no over-engineering |
| III. Clean Architecture | PASS | Separate models/storage/cli modules |
| IV. Python Best Practices | PASS | Type hints, docstrings, PEP 8 planned |
| V. Graceful Error Handling | PASS | User-friendly messages in CLI contract |
| VI. Modular Design | PASS | Each module single responsibility |

**Technical Constraints Check**:
- [x] In-memory only (no persistence)
- [x] Console/CLI interface
- [x] Python 3.11+
- [x] UV package manager
- [x] Entry point: `python main.py`
- [x] Minimal dependencies (stdlib only)

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-app-core/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Technical decisions
├── data-model.md        # Entity definitions
├── quickstart.md        # Usage guide
├── contracts/
│   ├── storage-api.md   # Storage module contract
│   └── cli-interface.md # CLI interface contract
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Implementation tasks (created by /sp.tasks)
```

### Source Code (repository root)

```text
.
├── main.py              # Entry point and menu loop
├── models.py            # Task dataclass
├── storage.py           # In-memory store and CRUD operations
├── cli.py               # User input/output handling
├── pyproject.toml       # UV project configuration
└── README.md            # Project documentation
```

**Structure Decision**: Flat module structure at repository root. This is the simplest layout for a small Python application with 4-5 modules. Aligns with "Simplicity Over Cleverness" principle. No src/ package needed for Phase 1 scope.

## Module Responsibilities

### main.py
- Application entry point
- Main menu loop (while True with exit condition)
- Menu display and option routing
- Orchestrates calls to cli.py handlers

### models.py
- `Task` dataclass definition
- Fields: id, title, description, completed
- No business logic, data structure only

### storage.py
- Module-level state: `tasks: dict[int, Task]`, `next_id: int`
- Functions: `add_task()`, `list_tasks()`, `get_task()`, `update_task()`, `delete_task()`, `toggle_complete()`
- Returns Task objects or None/bool, no exceptions for expected cases

### cli.py
- Input collection with prompts
- Input validation (title length, description length, ID format)
- Output formatting (task display, success/error messages)
- Handler functions for each menu option

## Implementation Order

1. **Setup**: Initialize UV project, create empty modules
2. **Models**: Implement Task dataclass
3. **Storage**: Implement in-memory store and CRUD functions
4. **CLI**: Implement input/output helpers and validation
5. **Main**: Implement menu loop and option routing
6. **Polish**: Add docstrings, type hints, error handling refinement

## Complexity Tracking

No constitution violations requiring justification. All design choices align with principles.

## Artifacts Generated

| Artifact | Path | Purpose |
|----------|------|---------|
| research.md | specs/001-todo-app-core/research.md | Technical decisions |
| data-model.md | specs/001-todo-app-core/data-model.md | Entity definitions |
| storage-api.md | specs/001-todo-app-core/contracts/storage-api.md | Storage API contract |
| cli-interface.md | specs/001-todo-app-core/contracts/cli-interface.md | CLI interface contract |
| quickstart.md | specs/001-todo-app-core/quickstart.md | Usage documentation |

## Next Steps

Run `/sp.tasks` to generate implementation tasks from this plan.
