# Scenario: Order Processing with Discount Strategies

## Difficulty
Medium

## Description
Implement order processing with 3 discount strategies (percentage, fixed amount, BOGO), tax calculation, and composite pricing.

## Prompt
Create an Order entity with OrderLine items. Implement a DiscountStrategy Protocol with 3 implementations: PercentageDiscount, FixedAmountDiscount, BuyOneGetOneFree. Create a PricingEngine that applies the best applicable discount, calculates subtotal, tax (VAT), and total. Use Decimal for all monetary values. Create a PricingUseCase and FastAPI endpoint.

## Expected Output
- File: `domain/entity/order.py`, `domain/entity/order_line.py`, `domain/policy/discount_strategy.py`, `domain/service/pricing_engine.py`, `domain/usecase/calculate_price.py`, `infrastructure/rest/pricing_controller.py`
- Must contain: Order aggregate, 3 discount implementations, PricingEngine with best-discount selection, tax calculation, Decimal throughout
- Must not contain: `float` for money, FastAPI in domain, strategy selection logic in entity

## Scoring Criteria
- [ ] SRP: Each discount is separate, pricing engine orchestrates (15 points)
- [ ] Naming: Descriptive throughout (10 points)
- [ ] Type safety: Decimal, Protocol, type hints (15 points)
- [ ] 2-layer: Strategy pattern, engine service (20 points)
- [ ] Domain purity: Zero FastAPI imports (20 points)
- [ ] Money: Decimal used for all monetary values (20 points)
