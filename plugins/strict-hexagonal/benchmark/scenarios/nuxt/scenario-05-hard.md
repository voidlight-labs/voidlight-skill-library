# Scenario: E-Commerce Dashboard

## Difficulty
Hard

## Description
Implement an e-commerce admin dashboard with orders, products, analytics, and fullstack domain architecture.

## Prompt
Create 4 domain entities: Order, Product, Customer, AnalyticsSummary with 10 branded types. Implement 3 domain services: OrderService, ProductService, AnalyticsService. Create 2 policy interfaces: PricingPolicy, ShippingPolicy with 2 implementations each. Create 5 Vue components with `script setup lang="ts"`: DashboardStats, OrderTable, ProductTable, CustomerList, RevenueChart. Create 4 server API routes with typed handlers. Create 2 composables: useDashboard, useOrders. Domain must be pure TypeScript with zero Nuxt/Vue/Pinia imports.

## Expected Output
- File: `domain/entity/*.ts`, `domain/entity/types.ts`, `domain/service/*.ts`, `domain/policy/*.ts`, `components/*.vue`, `server/api/*.ts`, `composables/*.ts`
- Must contain: 4 entities, 10 branded types, 3 services, 2 policies with 2 impls each, 5 components, 4 API routes, 2 composables
- Must not contain: `any`, domain logic in components, Nuxt imports in domain

## Scoring Criteria
- [ ] SRP: 4 entities, 3 services, 2 policies, 5 components (15 points)
- [ ] Naming: 10 branded types, highly descriptive (10 points)
- [ ] Type safety: No any, branded types, typed handlers (15 points)
- [ ] 2-layer: Multi-entity, policy pattern, services (20 points)
- [ ] Domain purity: Zero Nuxt/Vue/Pinia in domain (20 points)
- [ ] Fullstack: Proper server/client split (20 points)
