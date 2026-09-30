# Scenario: Task Manager with State Machine

## Difficulty
Easy

## Description
Implement a task management system with status transitions, validation, and CRUD operations.

## Prompt
Create a Task entity with id, title, description, status (todo, in_progress, done, archived), and due_date. Implement valid status transitions (todo→in_progress→done→archived, plus todo→archived). Create a TaskRepository port and a TaskService use case with methods for create, update status, and list. Use Pydantic for request/response DTOs in infrastructure only. Domain uses dataclasses.

## Expected Output
- File: `domain/entity/task.py`, `domain/port/task_repository.py`, `domain/usecase/task_service.py`, `infrastructure/rest/task_controller.py`
- Must contain: Task entity with status validation, TaskRepository Protocol, TaskService with 3 methods, FastAPI router
- Must not contain: FastAPI in domain, Pydantic in domain, mutable default args

## Scoring Criteria
- [ ] SRP: Status transitions, CRUD, validation separated (15 points)
- [ ] Naming: 3+ word function names (10 points)
- [ ] Type safety: Type hints, enum for status, Optional (15 points)
- [ ] 2-layer: Domain dataclasses, infra Pydantic (25 points)
- [ ] Domain purity: Zero FastAPI/Pydantic imports in domain (20 points)
- [ ] State machine: Valid transitions enforced (15 points)
