# Research: In-Memory Console Todo App

**Feature**: 001-todo-app-core
**Date**: 2026-01-05
**Status**: Complete

## Research Summary

This document captures technical decisions and research findings for the Phase 1 Todo application.

## Decision 1: Project Structure

**Decision**: Use flat module structure at repository root

**Rationale**:
- Simplest possible structure for a single-module Python application
- Aligns with constitution principle "Simplicity Over Cleverness"
- Entry point `main.py` at root satisfies `python main.py` requirement
- Separate modules (`models.py`, `storage.py`, `cli.py`) satisfy "Clean Architecture" principle

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| `src/` package structure | Over-engineering for 4-5 module app |
| Single-file application | Violates "Clean Architecture" and "Modular Design" principles |
| Nested package hierarchy | Unnecessary complexity for Phase 1 scope |

## Decision 2: Data Storage Pattern

**Decision**: Use module-level dictionary with auto-incrementing counter

**Rationale**:
- Dictionary provides O(1) lookup by ID (required for update/delete/toggle)
- Module-level state is simplest pattern for single-user, single-session app
- Counter variable handles ID auto-generation
- No external dependencies required

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| List with linear search | O(n) lookup inefficient, ID lookup is frequent operation |
| Class-based singleton | Over-engineering; module-level state sufficient |
| SQLite in-memory | External dependency, violates "minimal dependencies" constraint |

## Decision 3: Task Data Model

**Decision**: Use Python `dataclass` for Task entity

**Rationale**:
- Built-in Python feature (3.7+), no external dependencies
- Automatic `__init__`, `__repr__`, `__eq__` generation
- Type hints are inherent to dataclass definition
- Immutable option available if needed in future

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| Plain dictionary | No type safety, easy to introduce typos in keys |
| Named tuple | Immutable by default, updates require recreation |
| Pydantic model | External dependency not justified for Phase 1 |
| Regular class | More boilerplate than dataclass |

## Decision 4: Input Validation Strategy

**Decision**: Validate at CLI layer before passing to storage

**Rationale**:
- Single validation point prevents duplicate logic
- CLI layer is closest to user input
- Storage layer can assume valid data
- Aligns with "separation of concerns"

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| Validate in storage layer | CLI would still need validation for user messages |
| Validate in both layers | Duplicate logic, maintenance burden |
| Pydantic validation | External dependency not needed |

## Decision 5: CLI Menu Implementation

**Decision**: Simple while-loop with match-case (Python 3.10+)

**Rationale**:
- Clean, readable menu dispatch
- No external libraries needed
- Easy to extend with new options
- Native Python syntax

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| if-elif chain | Less readable than match-case |
| Click/Typer library | External dependency, over-engineering for simple menu |
| argparse subcommands | Different UX pattern than interactive menu |

## Decision 6: Error Handling Approach

**Decision**: Custom exception messages with try-except at CLI boundary

**Rationale**:
- Catch exceptions at CLI layer, display friendly messages
- Storage layer returns results (not raises for expected cases like "not found")
- Unexpected errors caught and displayed without stack trace
- Aligns with "Graceful Error Handling" principle

**Alternatives Considered**:
| Alternative | Rejected Because |
|-------------|------------------|
| Return error codes | Less Pythonic, harder to distinguish error types |
| Custom exception hierarchy | Over-engineering for 5 operations |
| Let exceptions propagate | Violates "no raw exceptions to users" |

## Technology Verification

| Technology | Version | Verified | Notes |
|------------|---------|----------|-------|
| Python | 3.11+ | Yes | Required by constitution |
| dataclasses | stdlib | Yes | Built-in since 3.7 |
| UV | latest | Yes | Package manager per constitution |

## Open Questions

None - all technical decisions resolved.

## References

- Python dataclasses: https://docs.python.org/3/library/dataclasses.html
- PEP 634 (match-case): https://peps.python.org/pep-0634/
- UV documentation: https://docs.astral.sh/uv/
