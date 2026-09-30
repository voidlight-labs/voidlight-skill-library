# Scenario: User Registration with Validation

## Difficulty
Easy

## Description
Implement user registration with email validation, password hashing delegation, and proper error handling.

## Prompt
Create a User entity with id, email, and hashed_password fields. Implement email format validation in domain. Create a PasswordHasher trait (domain) with infrastructure implementation. Use UserRepository trait for persistence. RegisterUserUseCase orchestrates validation, duplicate check, hashing, and storage. Return Result types throughout.

## Expected Output
- File: `src/domain/entity/user.rs`, `src/domain/port/user_repository.rs`, `src/domain/port/password_hasher.rs`, `src/domain/usecase/register_user.rs`, `src/infrastructure/persistence/*`, `src/infrastructure/rest/*`
- Must contain: User entity with validation, PasswordHasher trait, RegisterUserUseCase with Result returns
- Must not contain: `unwrap()` in production paths, Axum imports in domain, inline hashing logic

## Scoring Criteria
- [ ] SRP: Validation, duplicate check, hashing each separated (15 points)
- [ ] Naming: Descriptive names, no abbreviations (10 points)
- [ ] Type safety: Result<T,E>, thiserror, no unwrap (15 points)
- [ ] 2-layer: Trait-based ports, adapter pattern (25 points)
- [ ] Domain purity: Zero Axum/SQLx in domain (20 points)
- [ ] Error handling: Typed errors with codes (15 points)
