# Tasks: In-Memory Console Todo App

**Input**: Design documents from `/specs/001-todo-app-core/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/

**Tests**: No automated tests for Phase 1 (manual testing only per plan.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize UV project with `uv init` in repository root
- [x] T002 [P] Create empty models.py file at repository root
- [x] T003 [P] Create empty storage.py file at repository root
- [x] T004 [P] Create empty cli.py file at repository root
- [x] T005 [P] Create empty main.py file at repository root

**Checkpoint**: Project structure ready - all module files exist

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement Task dataclass in models.py with fields: id (int), title (str), description (str | None), completed (bool)
- [x] T007 Implement module-level storage state in storage.py: tasks dict and next_id counter
- [x] T008 Implement get_task(task_id: int) function in storage.py
- [x] T009 [P] Implement input validation helpers in cli.py: validate_title(), validate_description(), validate_id()
- [x] T010 [P] Implement output formatting helpers in cli.py: print_error(), print_success()

**Checkpoint**: Foundation ready - Task model and core utilities available for all stories

---

## Phase 3: User Story 1 - Add a New Task (Priority: P1)

**Goal**: Users can create new tasks with title and optional description

**Independent Test**: Launch app, select "Add Task", enter title, verify task created with unique ID

### Implementation for User Story 1

- [x] T011 [US1] Implement add_task(title, description) function in storage.py
- [x] T012 [US1] Implement handle_add_task() handler in cli.py with input prompts and validation
- [x] T013 [US1] Implement format_task_created() output function in cli.py

**Checkpoint**: User Story 1 complete - users can add tasks

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks with ID, title, status indicator, and description preview

**Independent Test**: Add several tasks, select "List Tasks", verify all display correctly

### Implementation for User Story 2

- [x] T014 [US2] Implement list_tasks() function in storage.py
- [x] T015 [US2] Implement format_task_list() output function in cli.py with status indicators (✓/✗)
- [x] T016 [US2] Implement handle_list_tasks() handler in cli.py

**Checkpoint**: User Stories 1 & 2 complete - MVP: users can add and view tasks

---

## Phase 5: User Story 6 - Navigate Menu and Exit (Priority: P1)

**Goal**: Users can navigate via menu and exit gracefully

**Independent Test**: Launch app, verify menu displays, test each option navigation, verify exit works

### Implementation for User Story 6

- [x] T017 [US6] Implement display_menu() function in cli.py with numbered options
- [x] T018 [US6] Implement get_menu_choice() function in cli.py with input validation
- [x] T019 [US6] Implement main menu loop in main.py with match-case routing
- [x] T020 [US6] Implement exit handler with farewell message in main.py

**Checkpoint**: Core MVP complete - users can add tasks, view tasks, and navigate menu

---

## Phase 6: User Story 3 - Toggle Task Completion (Priority: P2)

**Goal**: Users can mark tasks complete or incomplete by ID

**Independent Test**: Add task, toggle status, verify changes, toggle again to confirm reversion

### Implementation for User Story 3

- [x] T021 [US3] Implement toggle_complete(task_id) function in storage.py
- [x] T022 [US3] Implement handle_toggle_complete() handler in cli.py with ID prompt and validation
- [x] T023 [US3] Implement format_toggle_result() output function in cli.py

**Checkpoint**: User Story 3 complete - users can track task progress

---

## Phase 7: User Story 4 - Update Task Details (Priority: P3)

**Goal**: Users can update title and/or description of existing tasks

**Independent Test**: Add task, update title/description, verify changes persist

### Implementation for User Story 4

- [x] T024 [US4] Implement update_task(task_id, title, description) function in storage.py
- [x] T025 [US4] Implement handle_update_task() handler in cli.py with prompts for new values
- [x] T026 [US4] Implement format_update_result() output function in cli.py

**Checkpoint**: User Story 4 complete - users can modify tasks

---

## Phase 8: User Story 5 - Delete a Task (Priority: P3)

**Goal**: Users can remove tasks by ID

**Independent Test**: Add task, delete by ID, verify removed from list

### Implementation for User Story 5

- [x] T027 [US5] Implement delete_task(task_id) function in storage.py
- [x] T028 [US5] Implement handle_delete_task() handler in cli.py with ID prompt
- [x] T029 [US5] Implement format_delete_result() output function in cli.py

**Checkpoint**: User Story 5 complete - users can clean up tasks

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and documentation

- [x] T030 [P] Add docstrings to all public functions in models.py
- [x] T031 [P] Add docstrings to all public functions in storage.py
- [x] T032 [P] Add docstrings to all public functions in cli.py
- [x] T033 [P] Add docstrings to main.py entry point
- [x] T034 Verify all type hints are present and correct across all modules
- [x] T035 Run manual end-to-end test of all features per quickstart.md
- [x] T036 Update pyproject.toml with project metadata (name, version, description)

**Checkpoint**: All features complete, documented, and tested

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational (BLOCKS all user stories)
    ↓
┌───────────────────────────────────────┐
│  Phase 3: US1 (Add Task) - P1         │
│       ↓                               │
│  Phase 4: US2 (List Tasks) - P1       │
│       ↓                               │
│  Phase 5: US6 (Menu/Exit) - P1        │
│       ↓ (MVP Complete)                │
│  Phase 6: US3 (Toggle) - P2           │
│       ↓                               │
│  Phase 7: US4 (Update) - P3           │
│       ↓                               │
│  Phase 8: US5 (Delete) - P3           │
└───────────────────────────────────────┘
    ↓
Phase 9: Polish
```

### User Story Dependencies

| Story | Depends On | Can Start After |
|-------|------------|-----------------|
| US1 (Add) | Foundational | Phase 2 complete |
| US2 (List) | US1 | Phase 3 complete (needs tasks to list) |
| US6 (Menu) | US1, US2 | Phase 4 complete (menu routes to handlers) |
| US3 (Toggle) | US6 | Phase 5 complete (needs menu integration) |
| US4 (Update) | US6 | Phase 5 complete (needs menu integration) |
| US5 (Delete) | US6 | Phase 5 complete (needs menu integration) |

### Within Each Phase

- Models before storage functions
- Storage functions before CLI handlers
- CLI handlers before main.py integration

### Parallel Opportunities

**Phase 1 (all parallelizable)**:
```
T002, T003, T004, T005 - Create empty module files
```

**Phase 2**:
```
T009, T010 - Validation and output helpers (after T006-T008)
```

**Phase 9 (all parallelizable)**:
```
T030, T031, T032, T033 - Add docstrings to all modules
```

---

## Implementation Strategy

### MVP First (Phases 1-5)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: US1 (Add Task)
4. Complete Phase 4: US2 (List Tasks)
5. Complete Phase 5: US6 (Menu/Exit)
6. **STOP and VALIDATE**: Test MVP end-to-end
7. Run `python main.py` and verify add + list + menu works

### Incremental Delivery

| Milestone | Phases | Features |
|-----------|--------|----------|
| MVP | 1-5 | Add, List, Menu |
| Core Complete | 6 | + Toggle |
| Full Feature | 7-8 | + Update, Delete |
| Release Ready | 9 | + Documentation |

### Suggested Execution Commands

```bash
# After each phase, verify:
python main.py

# After Phase 5 (MVP), test:
# 1. Add a task with title only
# 2. Add a task with title and description
# 3. List tasks (verify both appear)
# 4. Exit application

# After Phase 9 (Complete), run full quickstart.md validation
```

---

## Task Summary

| Phase | Tasks | Parallel | Description |
|-------|-------|----------|-------------|
| 1 | 5 | 4 | Setup |
| 2 | 5 | 2 | Foundational |
| 3 | 3 | 0 | US1: Add Task |
| 4 | 3 | 0 | US2: List Tasks |
| 5 | 4 | 0 | US6: Menu/Exit |
| 6 | 3 | 0 | US3: Toggle |
| 7 | 3 | 0 | US4: Update |
| 8 | 3 | 0 | US5: Delete |
| 9 | 7 | 4 | Polish |
| **Total** | **36** | **10** | |

---

## Notes

- All tasks include exact file paths
- [P] marked tasks can run in parallel within their phase
- [USx] labels map tasks to user stories for traceability
- Commit after each task or logical group
- Stop at any checkpoint to validate independently
- MVP (Phases 1-5) delivers working add + list + menu functionality
