# Scenario: Shopping Cart with State Management

## Difficulty
Medium

## Description
Implement a shopping cart with Pinia, domain layer, composable, and multi-component architecture.

## Prompt
Create a Cart domain entity with CartItem (4 branded types: CartId, ProductId, ProductName, Quantity). Implement 8 cart operations as pure domain functions (addItem, removeItem, updateQuantity, clearCart, getItemCount, getTotalItems, isEmpty, getCartTotal). Create a CartStore Pinia store that wraps the domain logic. Create 3 Vue components: CartSidebar, CartItem, AddToCartButton. Create a `useCart` composable exposing store methods. Domain must be pure TypeScript.

## Expected Output
- File: `domain/entity/cart.ts`, `domain/entity/types.ts`, `stores/cartStore.ts`, `composables/useCart.ts`, `components/CartSidebar.vue`, `components/CartItem.vue`, `components/AddToCartButton.vue`
- Must contain: Cart entity, 4 branded types, 8 pure functions, Pinia store, composable, 3 components
- Must not contain: `any`, domain logic in components, Nuxt imports in domain

## Scoring Criteria
- [ ] SRP: 8 functions, store, composable, 3 components (15 points)
- [ ] Naming: 4 branded types, descriptive names (10 points)
- [ ] Type safety: Branded types, no any, typed store (15 points)
- [ ] 2-layer: Pinia as infra wrapper around domain (20 points)
- [ ] Domain purity: Zero Nuxt/Vue/Pinia in domain (20 points)
- [ ] Components: Logic in composable/store, not components (20 points)
