# Scenario: Shopping Cart with Optimistic Updates

## Difficulty
Medium

## Description
Implement a shopping cart with optimistic UI, Server Actions, domain validation, and proper Next.js architecture.

## Prompt
Create a Cart entity with 4 branded types (CartId, ProductId, Quantity, PriceCents). Implement 8 pure domain functions: addItem, removeItem, updateQuantity, getItemCount, getTotalPrice, applyPromoCode, removePromoCode, validateCart. Create a CartService orchestrating operations. Create 3 Server Actions: addToCart, removeFromCart, updateQuantity. Create a CartPage Server Component and a CartItemList Client Component with optimistic updates via `useOptimistic`. Domain pure TypeScript.

## Expected Output
- File: `domain/entity/cart.ts`, `domain/entity/types.ts`, `domain/service/cartService.ts`, `domain/port/cartRepository.ts`, `app/cart/page.tsx`, `components/CartItemList.tsx`, `app/cart/actions.ts`
- Must contain: Cart entity, 4 branded types, 8 pure functions, CartService, 3 Server Actions, Server Component, Client Component with useOptimistic
- Must not contain: `any`, domain logic in components, Next.js in domain

## Scoring Criteria
- [ ] SRP: 8 functions, service, actions, components (15 points)
- [ ] Naming: 4 branded types, descriptive names (10 points)
- [ ] Type safety: No any, branded types, typed actions (15 points)
- [ ] 2-layer: Service pattern, Server Actions (20 points)
- [ ] Domain purity: Zero Next.js/React in domain (20 points)
- [ ] Optimistic: useOptimistic for UI updates (20 points)
