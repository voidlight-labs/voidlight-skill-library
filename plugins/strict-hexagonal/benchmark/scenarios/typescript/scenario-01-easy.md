# Scenario: User Registration Validation

## Difficulty
Easy

## Description
Implement user registration with branded types, pure domain validation, and Express controller.

## Prompt
Create branded types for UserId, Email, and UserName. Implement pure domain validation functions for email format and password strength. Create a UserRepository interface and a RegisterUserUseCase returning Result types. Implement an Express controller with zod validation at the boundary. Domain must be pure TypeScript with zero Express/Prisma imports.

## Expected Output
- File: `domain/entity/types.ts`, `domain/entity/user.ts`, `domain/port/userRepository.ts`, `domain/usecase/registerUser.ts`, `infrastructure/persistence/prismaUserRepository.ts`, `infrastructure/rest/userController.ts`
- Must contain: 3 branded types, validation functions, Result type, use case, Prisma adapter, Express controller with zod
- Must not contain: `any` type, `null` without Option, Express imports in domain

## Scoring Criteria
- [ ] SRP: Validation, registration, persistence each separate (15 points)
- [ ] Naming: 3+ word function names (10 points)
- [ ] Type safety: Branded types, Result, no any (15 points)
- [ ] 2-layer: Domain pure, infra has Express/Prisma (25 points)
- [ ] Domain purity: Zero Express/Prisma imports in domain (20 points)
- [ ] Validation: Pure domain validation + zod at boundary (15 points)
