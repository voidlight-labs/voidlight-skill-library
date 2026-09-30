# Scenario: Inventory Management with Policy Engine

## Difficulty
Medium

## Description
Implement inventory reservation with a pluggable policy engine, multiple domain event types, and conditional event publishing.

## Prompt
Create an Inventory aggregate with StockItem entities. Implement a ReservationPolicy interface with two implementations: StandardReservationPolicy and BulkReservationPolicy. Create domain events: StockReservedEvent, InsufficientStockEvent, LowStockAlertEvent. Use a Specification pattern for low-stock detection. The ReserveStockUseCase should select the appropriate policy based on order size and publish the correct events.

## Expected Output
- File: `domain/entity/Inventory.java`, `domain/entity/StockItem.java`, `domain/policy/ReservationPolicy.java`, `domain/event/*Event.java`, `domain/port/*Repository.java`, `domain/usecase/ReserveStockUseCase.java`
- Must contain: Inventory aggregate, policy interface + implementations, 4 event types, specification for low-stock, use case with policy selection
- Must not contain: SQL in domain, framework annotations in domain, policy implementations calling repository directly

## Scoring Criteria
- [ ] SRP: Policy engine, events, specification each separate (10 points)
- [ ] Naming: 3+ word function names, descriptive class names (10 points)
- [ ] Type safety: Interfaces, generics, Optional (10 points)
- [ ] 2-layer: Policy and specification patterns (25 points)
- [ ] Domain purity: Zero framework imports (20 points)
- [ ] Events: Multiple event types with conditional publishing (25 points)
