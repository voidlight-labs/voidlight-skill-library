# Scenario: Shopping Cart with Inventory

## Difficulty
Medium

## Description
Implement shopping cart with inventory validation, branded types, and complex domain logic.

## Prompt
Create a Cart aggregate with 6 branded types (CartId, ProductId, ProductName, Quantity, PriceCents, PromoCode). Implement 12 cart operation functions: addItem, removeItem, updateQuantity, clearCart, applyPromo, removePromo, calculateSubtotal, calculateDiscount, calculateTax, calculateShipping, calculateTotal, validateCart. Create an InventoryService interface for async stock validation. Implement Prisma adapter and Express handlers with 5 routes.

## Expected Output
- File: `domain/entity/cart.ts`, `domain/entity/types.ts`, `domain/service/inventoryService.ts`, `domain/port/cartRepository.ts`, `domain/usecase/cartUseCases.ts`, `infrastructure/persistence/prismaCartRepository.ts`, `infrastructure/rest/cartRouter.ts`
- Must contain: Cart aggregate, 6 branded types, 12 functions, InventoryService interface, promo logic, Prisma adapter
- Must not contain: `any`, Express in domain, inline calculations

## Scoring Criteria
- [ ] SRP: 12 functions, each single responsibility (15 points)
- [ ] Naming: Highly descriptive 3+ word names (10 points)
- [ ] Type safety: 6 branded types, Result, no any (15 points)
- [ ] 2-layer: Inventory service interface, async validation (20 points)
- [ ] Domain purity: Zero Express/Prisma in domain (20 points)
- [ ] Cart logic: Promo, tax, shipping, validation (20 points)
