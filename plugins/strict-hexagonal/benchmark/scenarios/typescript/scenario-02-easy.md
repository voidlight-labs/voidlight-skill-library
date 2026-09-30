# Scenario: Order Pricing Calculator

## Difficulty
Easy

## Description
Implement order pricing with branded types, separate calculation functions, and Express endpoint.

## Prompt
Create branded types for OrderId, Money (as cents), and Quantity. Implement separate pure functions for: calculateLineItemSubtotal, calculateCartSubtotal, applyDiscount, calculateTax, calculateTotal. Each function single responsibility. Create an Express router with a POST endpoint. Use explicit return types everywhere.

## Expected Output
- File: `domain/entity/types.ts`, `domain/service/pricing.ts`, `infrastructure/rest/pricingController.ts`
- Must contain: 3 branded types, 5 pure calculation functions, Express route handler
- Must not contain: `any` type, `float` for money (use integer cents), inline calculations in controller

## Scoring Criteria
- [ ] SRP: 5 separate calculation functions (15 points)
- [ ] Naming: Descriptive 3+ word names (10 points)
- [ ] Type safety: Branded types, explicit returns, no any (15 points)
- [ ] 2-layer: Pure domain functions, Express in infra (25 points)
- [ ] Domain purity: Zero Express/Prisma in domain (20 points)
- [ ] Money: Integer cents, not float (15 points)
