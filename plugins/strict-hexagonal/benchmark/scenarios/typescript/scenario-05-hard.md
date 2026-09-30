# Scenario: Library Book Lending System

## Difficulty
Hard

## Description
Implement a library lending system with 3 aggregates, 3 repository interfaces, domain events, and full transaction-like orchestration.

## Prompt
Create 3 aggregates: Book (with ISBN, title, status), Member (with id, name, loan limit), Loan (with book, member, due date, return date). Implement 3 domain services: borrowBook, returnBook, checkOverdueLoans. Create 3 repository interfaces (BookRepository, MemberRepository, LoanRepository) with Prisma implementations. Implement 3 Express controllers. Include fine calculation ($0.50/day overdue), loan limit enforcement (max 5 books), and reservation queue. Use 9 branded types throughout.

## Expected Output
- File: `domain/entity/book.ts`, `domain/entity/member.ts`, `domain/entity/loan.ts`, `domain/entity/types.ts`, `domain/service/*.ts`, `domain/port/*.ts`, `domain/usecase/*.ts`, `infrastructure/persistence/*.ts`, `infrastructure/rest/*.ts`
- Must contain: 3 aggregates, 9 branded types, 3 domain services, 3 repository interfaces, 3 Prisma implementations, fine calculation, loan limits
- Must not contain: `any`, Express in domain, Prisma in domain, circular imports

## Scoring Criteria
- [ ] SRP: 3 aggregates, 3 services, 3 repos each separate (15 points)
- [ ] Naming: 9 branded types, descriptive names (10 points)
- [ ] Type safety: 9 branded types, Result, no any (15 points)
- [ ] 2-layer: 3-aggregate architecture, event-like orchestration (20 points)
- [ ] Domain purity: Zero Express/Prisma in domain (20 points)
- [ ] Business rules: Fines, limits, reservations enforced (20 points)
