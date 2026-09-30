# Scenario: Todo List with Server Actions

## Difficulty
Easy

## Description
Implement a todo list with Next.js App Router, Server Actions, and 2-layer clean architecture.

## Prompt
Create a Todo domain entity (id, title, completed) and TodoRepository interface in `domain/`. Create a Server Action for adding todos. Create a Server Component page displaying todos. Create a Client Component form using the Server Action. Use `revalidatePath` after mutations. Domain must be pure TypeScript with zero Next.js/React imports.

## Expected Output
- File: `domain/entity/todo.ts`, `domain/port/todoRepository.ts`, `app/todos/page.tsx`, `app/todos/actions.ts`, `components/TodoForm.tsx`
- Must contain: Todo entity, TodoRepository interface, Server Action, Server Component, Client Component form
- Must not contain: `any` type, React hooks in domain, Next.js imports in domain

## Scoring Criteria
- [ ] SRP: Entity, repository, action, page, form each separate (15 points)
- [ ] Naming: Descriptive names (10 points)
- [ ] Type safety: No any, typed actions, branded types (15 points)
- [ ] 2-layer: Domain pure, Next.js in infra (25 points)
- [ ] Domain purity: Zero Next.js/React imports in domain (20 points)
- [ ] Server actions: Proper mutation with revalidation (15 points)
