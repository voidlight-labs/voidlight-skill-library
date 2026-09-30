# Scenario: Product Catalog with Filtering

## Difficulty
Medium

## Description
Implement a product catalog with filtering, pagination, domain services, and Next.js patterns.

## Prompt
Create a Product entity with 5 branded types (ProductId, ProductName, Price, Category, Brand). Implement a ProductFilter value object and a ProductSearchService with 6 pure functions: filterByCategory, filterByPriceRange, filterByBrand, sortByPrice, sortByName, paginateResults. Create a Server Component with `unstable_cache` for product listing. Create a Client Component filter sidebar with `useState`. Create a Server Action for search. Domain pure TypeScript.

## Expected Output
- File: `domain/entity/product.ts`, `domain/entity/types.ts`, `domain/valueObject/productFilter.ts`, `domain/service/productSearch.ts`, `domain/port/productRepository.ts`, `app/products/page.tsx`, `components/FilterSidebar.tsx`, `app/products/actions.ts`
- Must contain: Product entity, 5 branded types, ProductFilter VO, 6 pure functions, Server Component with cache, Client filter, Server Action
- Must not contain: `any`, domain logic in components, Next.js in domain

## Scoring Criteria
- [ ] SRP: 6 search functions, VO, cache, filter component (15 points)
- [ ] Naming: 5 branded types, descriptive names (10 points)
- [ ] Type safety: No any, branded types, typed filter (15 points)
- [ ] 2-layer: Value object, service pattern, caching (20 points)
- [ ] Domain purity: Zero Next.js/React in domain (20 points)
- [ ] Next.js: unstable_cache, Server/Client split (20 points)
