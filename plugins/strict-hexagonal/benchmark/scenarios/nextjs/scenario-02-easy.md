# Scenario: User Profile Display

## Difficulty
Easy

## Description
Implement user profile display with Server Component, domain types, and proper Next.js patterns.

## Prompt
Create UserProfile entity with 4 branded types (UserId, DisplayName, Email, Bio). Implement a UserRepository interface and a GetUserProfileUseCase. Create a Server Component at `app/profile/[id]/page.tsx` that fetches and displays the profile. Create a `not-found.tsx` for missing profiles. Domain must be pure TypeScript.

## Expected Output
- File: `domain/entity/userProfile.ts`, `domain/entity/types.ts`, `domain/port/userRepository.ts`, `domain/usecase/getUserProfile.ts`, `app/profile/[id]/page.tsx`, `app/profile/[id]/not-found.tsx`
- Must contain: UserProfile entity, 4 branded types, use case, Server Component, not-found boundary
- Must not contain: `any`, `useEffect` in Server Component, Next.js imports in domain

## Scoring Criteria
- [ ] SRP: Entity, use case, page, not-found each separate (15 points)
- [ ] Naming: 4 branded types, descriptive names (10 points)
- [ ] Type safety: Branded types, no any, typed params (15 points)
- [ ] 2-layer: Domain pure, Next.js in infra (25 points)
- [ ] Domain purity: Zero Next.js/React imports in domain (20 points)
- [ ] Patterns: Server Component, error boundary (15 points)
