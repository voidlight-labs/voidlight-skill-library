# Scenario: E-Commerce Cart and Checkout Engine

## Difficulty
Hard

## Description
Implement a full e-commerce cart and checkout engine across 5 domain modules with shipping, tax, multi-discount, and inventory management.

## Prompt
Create a complete e-commerce domain: Product aggregate, Cart aggregate with CartItem, PricingEngine with shipping cost calculation (by weight/destination), best-discount selection (multiple discounts, pick best), tax calculation, stock reservation and deduction, order composition from cart. Split across 5 domain files: products, cart, pricing, inventory, orders. Each module independent. Use Decimal for all money, datetime with timezone for timestamps. Create 4 use cases: AddToCart, ApplyPromoCode, CalculateCheckout, PlaceOrder.

## Expected Output
- File: `domain/entity/product.py`, `domain/entity/cart.py`, `domain/service/pricing_engine.py`, `domain/service/inventory_service.py`, `domain/entity/order.py`, `domain/usecase/*.py`, `infrastructure/rest/*.py`
- Must contain: 5 domain modules, shipping calculator, multi-discount selector, tax engine, stock reservation, 4 use cases
- Must not contain: Any framework imports in domain, `float` for money, circular imports

## Scoring Criteria
- [ ] SRP: 5 modules, each with single responsibility (15 points)
- [ ] Naming: Highly descriptive throughout (10 points)
- [ ] Type safety: Decimal, datetime with tz, generics (15 points)
- [ ] 2-layer: Multi-module domain, 4 use cases (20 points)
- [ ] Domain purity: Zero framework imports across 5 modules (20 points)
- [ ] Architecture: No circular imports, proper dependency direction (20 points)
