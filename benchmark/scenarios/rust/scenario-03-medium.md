# Scenario: Inventory Management with Stock Operations

## Difficulty
Medium

## Description
Implement inventory management with stock operations, transaction log, and concurrent access patterns.

## Prompt
Create an Inventory aggregate with StockItem entities. Implement stock operations: add_stock, remove_stock, reserve_stock, release_reservation. Use tokio::sync::Mutex for concurrent access in infrastructure. Create domain events for stock changes. Implement a StockLevelPolicy for minimum stock alerts. Use Result chains with `and_then` / `map_err`.

## Expected Output
- File: `src/domain/entity/inventory.rs`, `src/domain/entity/stock_item.rs`, `src/domain/event/stock_changed.rs`, `src/domain/policy/stock_level_policy.rs`, `src/domain/port/*`, `src/domain/usecase/*.rs`, `src/infrastructure/*.rs`
- Must contain: Inventory aggregate, StockItem, 4 operations, domain events, stock policy, concurrent adapter
- Must not contain: `unwrap()` in domain, SQLx in domain, direct DB access from domain

## Scoring Criteria
- [ ] SRP: Each operation, policy, event separate (15 points)
- [ ] Naming: 3+ word names, descriptive types (10 points)
- [ ] Type safety: Result chains, thiserror, no unwrap (15 points)
- [ ] 2-layer: Aggregate root, events, policy pattern (20 points)
- [ ] Domain purity: Zero framework imports in domain (20 points)
- [ ] Concurrency: Proper locking in infra, pure domain (20 points)
