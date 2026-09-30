# Scenario: E-Commerce Checkout Flow

## Difficulty
Hard

## Description
Implement a full e-commerce checkout with cart, pricing, inventory, payment, and order composition.

## Prompt
Create a complete checkout system: Cart aggregate with CartItem, CheckoutService orchestrating the flow, PricingEngine with discount strategies (percentage, fixed, BOGO), ShippingCalculator by weight/destination, PaymentPort trait for gateway abstraction, InventoryService for stock reservation. Implement rollback on payment failure. Use 8 pure domain functions, 3 repository traits, and a CheckoutService. All errors use thiserror with machine-readable codes.

## Expected Output
- File: `src/domain/entity/cart.rs`, `src/domain/entity/cart_item.rs`, `src/domain/service/checkout_service.rs`, `src/domain/service/pricing_engine.rs`, `src/domain/service/shipping_calculator.rs`, `src/domain/port/payment_port.rs`, `src/domain/port/*repository.rs`, `src/domain/event/*.rs`, `src/infrastructure/*.rs`
- Must contain: Cart aggregate, CheckoutService, 3 discount strategies, shipping calc, PaymentPort, inventory service, rollback, 8+ domain functions
- Must not contain: `unwrap()` in domain, Axum/SQLx in domain, payment SDK in domain

## Scoring Criteria
- [ ] SRP: 8+ domain functions, each single responsibility (15 points)
- [ ] Naming: Highly descriptive, no abbreviations (10 points)
- [ ] Type safety: Result chains, traits, thiserror, no unwrap (15 points)
- [ ] 2-layer: Multiple services, 3 repository traits (20 points)
- [ ] Domain purity: Zero Axum/SQLx/payment SDK in domain (20 points)
- [ ] Orchestration: Checkout flow with rollback (20 points)
