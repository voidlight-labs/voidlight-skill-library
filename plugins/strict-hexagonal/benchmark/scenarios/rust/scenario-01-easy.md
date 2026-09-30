# Scenario: Todo List API

## Difficulty
Easy

## Description
Implement a Todo List API with Axum and SQLx following 2-layer clean architecture.

## Prompt
Create a TodoItem entity with id, title, completed status, and created_at. Implement a TodoRepository trait and a CreateTodoUseCase. Create a SqlxTodoRepository in infrastructure. Use Axum Router with handlers. Domain must be pure Rust with zero Axum/SQLx imports. Use thiserror for domain errors.

## Expected Output
- File: `src/domain/entity/todo.rs`, `src/domain/port/todo_repository.rs`, `src/domain/usecase/create_todo.rs`, `src/infrastructure/persistence/sqlx_todo_repository.rs`, `src/infrastructure/rest/todo_handler.rs`
- Must contain: TodoItem struct, TodoRepository trait, CreateTodoUseCase, SQLx adapter, Axum handlers
- Must not contain: `unwrap()` in domain, Axum imports in domain, SQLx in domain

## Scoring Criteria
- [ ] SRP: Entity, repository, use case, adapter each separate (15 points)
- [ ] Naming: Descriptive 3+ word names (10 points)
- [ ] Type safety: thiserror, explicit types, no unwrap in domain (15 points)
- [ ] 2-layer: Domain pure, infra has Axum/SQLx (25 points)
- [ ] Domain purity: Zero Axum/SQLx imports in domain (20 points)
- [ ] Errors: thiserror enum with machine-readable codes (15 points)
