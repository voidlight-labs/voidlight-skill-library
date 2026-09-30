# Scenario: Product Catalog Page

## Difficulty
Easy

## Description
Implement a product catalog page with domain layer, composable, and Nuxt server API route.

## Prompt
Create a Product domain entity (id, name, price) and ProductRepository interface in `domain/`. Create a `useProducts` composable that fetches products via `useFetch`. Create a Nuxt server API route at `server/api/products.get.ts` that returns products. Create a `pages/catalog.vue` page displaying the product list. Domain must be pure TypeScript with zero Nuxt/Vue imports.

## Expected Output
- File: `domain/entity/product.ts`, `domain/port/productRepository.ts`, `composables/useProducts.ts`, `server/api/products.get.ts`, `pages/catalog.vue`
- Must contain: Product entity, ProductRepository interface, composable with useFetch, server route, Vue page
- Must not contain: `any` type, Nuxt imports in domain, logic in component

## Scoring Criteria
- [ ] SRP: Entity, repository, composable, page each separate (15 points)
- [ ] Naming: Descriptive names (10 points)
- [ ] Type safety: No any, typed interfaces, generics on ref (15 points)
- [ ] 2-layer: Domain pure, infra has Nuxt/Vue (25 points)
- [ ] Domain purity: Zero Nuxt/Vue imports in domain (20 points)
- [ ] Composable: Shared logic extracted from component (15 points)
