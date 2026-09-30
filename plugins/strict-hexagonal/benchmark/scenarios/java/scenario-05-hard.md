# Scenario: E-Commerce Checkout Flow

## Difficulty
Hard

## Description
Implement a full e-commerce checkout flow with Cart aggregate, multiple use cases, discount/tax policy engine, payment initiation, inventory reservation with rollback, and comprehensive domain events.

## Prompt
Create a complete checkout system: Cart aggregate with CartItem value objects, DiscountPolicy interface (percentage, fixed amount, BOGO implementations), TaxCalculator interface, PaymentPort for payment gateway abstraction. Implement use cases: AddToCartUseCase, ApplyDiscountUseCase, CalculateTotalsUseCase, InitiateCheckoutUseCase (which orchestrates inventory reservation, payment, and order creation). Include rollback mechanism for failed payments. Generate 6 domain event types and 9 typed domain exceptions. All monetary values use BigDecimal.

## Expected Output
- File: `domain/entity/Cart.java`, `domain/entity/CartItem.java`, `domain/policy/DiscountPolicy.java`, `domain/policy/TaxCalculator.java`, `domain/port/PaymentPort.java`, `domain/port/CartRepository.java`, `domain/event/*.java`, `domain/exception/*.java`, `domain/usecase/*.java`
- Must contain: Cart aggregate, 3 discount implementations, tax calculator, payment port, 5 use cases, 6 events, 9 exceptions, rollback logic
- Must not contain: Any framework imports in domain, payment gateway SDK in domain, HTTP status codes in domain exceptions

## Scoring Criteria
- [ ] SRP: Each use case, policy, calculator is separate (10 points)
- [ ] Naming: Highly descriptive throughout (10 points)
- [ ] Type safety: BigDecimal everywhere, sealed types, generics (10 points)
- [ ] 2-layer: Full architecture with 5+ use cases (25 points)
- [ ] Domain purity: Zero framework/Spring/Quarkus imports (20 points)
- [ ] Complexity: Rollback, orchestration, 6 events, 9 exceptions (25 points)
