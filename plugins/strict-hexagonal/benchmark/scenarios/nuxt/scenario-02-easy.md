# Scenario: User Profile Form

## Difficulty
Easy

## Description
Implement a user profile form with validation, domain types, and proper TypeScript in Nuxt.

## Prompt
Create UserProfile entity with 5 branded types (UserId, DisplayName, Bio, AvatarUrl, JoinDate). Implement pure validation functions for display name (3-50 chars) and bio (0-500 chars). Create a `useUserProfile` composable with `updateProfile` method. Create a profile edit page with `script setup lang="ts"` using the composable. Domain must be pure TypeScript.

## Expected Output
- File: `domain/entity/userProfile.ts`, `domain/entity/types.ts`, `composables/useUserProfile.ts`, `pages/profile/edit.vue`
- Must contain: 5 branded types, validation functions, composable, form page with typed refs
- Must not contain: `any` type, `ref()` without generic, Nuxt imports in domain

## Scoring Criteria
- [ ] SRP: Validation, composable, form each separate (15 points)
- [ ] Naming: 5 branded types, descriptive names (10 points)
- [ ] Type safety: Branded types, ref<string>(), no any (15 points)
- [ ] 2-layer: Domain pure, Vue in infra (25 points)
- [ ] Domain purity: Zero Nuxt/Vue imports in domain (20 points)
- [ ] Validation: Pure domain validation functions (15 points)
