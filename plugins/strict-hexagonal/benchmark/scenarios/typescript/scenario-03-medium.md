# Scenario: Task Management with Status Workflow

## Difficulty
Medium

## Description
Implement task management with status workflow, branded types, and full 2-layer architecture.

## Prompt
Create a Task aggregate with 4 branded types (TaskId, UserId, Title, Description). Implement a status workflow: todo → in-progress → done → archived, with validation. Create 5 transition functions (start, complete, archive, reopen, assign). Implement a TaskRepository with full CRUD, Prisma adapter with conversion helpers, and Express router factory with 6 routes.

## Expected Output
- File: `domain/entity/task.ts`, `domain/entity/types.ts`, `domain/port/taskRepository.ts`, `domain/usecase/taskUseCases.ts`, `infrastructure/persistence/prismaTaskRepository.ts`, `infrastructure/rest/taskRouter.ts`
- Must contain: Task aggregate, 4 branded types, 5 transition functions, workflow validation, Prisma adapter, Express router
- Must not contain: `any`, Express in domain, Prisma in domain, invalid transitions

## Scoring Criteria
- [ ] SRP: 5 transitions, CRUD, validation each separate (15 points)
- [ ] Naming: Descriptive names with qualifiers (10 points)
- [ ] Type safety: 4 branded types, Result, no any (15 points)
- [ ] 2-layer: Full workflow, repository pattern (20 points)
- [ ] Domain purity: Zero Express/Prisma in domain (20 points)
- [ ] Workflow: Valid transitions enforced (20 points)
