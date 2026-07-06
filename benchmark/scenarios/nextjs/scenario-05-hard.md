# Scenario: E-Commerce Admin Panel

## Difficulty
Hard

## Description
Implement an admin panel with CRUD, analytics, role-based access, and full Next.js architecture.

## Prompt
Create 4 domain entities: Product, Order, Customer, AdminUser with 8 branded types. Implement 4 domain services: ProductService, OrderService, CustomerService, AnalyticsService. Create 2 policy interfaces: AccessControlPolicy, DataRetentionPolicy with implementations. Create 4 Server Components with async data fetching: DashboardPage, ProductsPage, OrdersPage, CustomersPage. Create 6 Server Actions for CRUD. Create 3 Client Components with forms: ProductForm, OrderStatusForm, CustomerEditForm. Domain pure TypeScript.

## Expected Output
- File: `domain/entity/*.ts`, `domain/entity/types.ts`, `domain/service/*.ts`, `domain/policy/*.ts`, `app/admin/*/page.tsx`, `app/admin/*/actions.ts`, `components/*Form.tsx`
- Must contain: 4 entities, 8 branded types, 4 services, 2 policies with impls, 4 Server Components, 6 Server Actions, 3 Client Components
- Must not contain: `any`, domain logic in components, Next.js in domain

## Scoring Criteria
- [ ] SRP: 4 entities, 4 services, 2 policies, 7 components (15 points)
- [ ] Naming: 8 branded types, highly descriptive (10 points)
- [ ] Type safety: No any, branded types, typed forms (15 points)
- [ ] 2-layer: Multi-entity, policy pattern, services (20 points)
- [ ] Domain purity: Zero Next.js/React in domain (20 points)
- [ ] Admin patterns: CRUD, Server/Client split (20 points)
