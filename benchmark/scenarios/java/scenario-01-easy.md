# Scenario: Product Catalog CRUD

## Difficulty
Easy

## Description
Implement a basic Product entity with CRUD operations following 2-layer clean architecture. Tests fundamental domain/infrastructure separation.

## Prompt
Create a Product domain entity with id, name, price, and stockQuantity fields. Implement a ProductRepository port interface and a CreateProductUseCase. Then implement an in-memory ProductRepository adapter in the infrastructure layer. Use Java with proper typing, explicit naming, and 2-layer architecture. Domain layer must have zero Spring/Quarkus imports.

## Expected Output
- File: `domain/entity/Product.java`, `domain/port/ProductRepository.java`, `domain/usecase/CreateProductUseCase.java`, `infrastructure/persistence/InMemoryProductRepository.java`
- Must contain: Product entity with validation, ProductRepository interface, CreateProductUseCase, InMemoryProductRepository implementing the port
- Must not contain: `@Entity` in domain, `@Autowired` on fields, `null` returns without Optional, Spring imports in domain

## Scoring Criteria
- [ ] SRP: Each class has single responsibility (10 points)
- [ ] Naming: Descriptive 3+ word function names (10 points)
- [ ] Type safety: Optional<T> for nullable, BigDecimal for price (15 points)
- [ ] 2-layer: Domain pure native, infra has framework (30 points)
- [ ] Domain purity: Zero Spring/Quarkus/JPA imports in domain (20 points)
- [ ] Testing: Testable with mock port implementations (15 points)
