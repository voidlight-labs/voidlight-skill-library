# Scenario: User Registration

## Difficulty
Easy

## Description
Implement user registration with validation, duplicate checks, and password hashing delegation following SRP.

## Prompt
Create a UserRegistrationUseCase that validates email format, checks for duplicate users via a UserRepository port, and delegates password hashing to a PasswordHasher interface. Use Java records for DTOs, Optional for nullable returns, and constructor injection. Domain must be pure Java with zero framework imports.

## Expected Output
- File: `domain/entity/User.java`, `domain/port/UserRepository.java`, `domain/service/PasswordHasher.java`, `domain/usecase/RegisterUserUseCase.java`
- Must contain: User entity with email validation, UserRepository port, PasswordHasher interface (domain), RegisterUserUseCase orchestrating the flow
- Must not contain: Spring annotations in domain, `null` returns, inline password hashing logic in use case

## Scoring Criteria
- [ ] SRP: Validation, duplicate check, hashing each separated (10 points)
- [ ] Naming: Explicit function names (10 points)
- [ ] Type safety: Optional, records, typed exceptions (15 points)
- [ ] 2-layer: Domain pure, infra adapts (30 points)
- [ ] Domain purity: Zero framework imports in domain (20 points)
- [ ] Error handling: Typed domain exceptions (15 points)
