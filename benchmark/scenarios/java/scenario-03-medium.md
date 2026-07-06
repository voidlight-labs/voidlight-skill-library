# Scenario: Order Processing with Domain Events

## Difficulty
Medium

## Description
Implement order processing with Order and OrderLine entities, aggregate root pattern, and domain events for decoupled cross-aggregate communication.

## Prompt
Create an Order aggregate root containing OrderLine value objects. Implement OrderPlacedEvent as a domain event. Create a PlaceOrderUseCase that saves the order and publishes the event via an EventPublisher port. Include an InventoryReservationService that listens to the event (demonstrated via event handler in infrastructure). Use BigDecimal for monetary values, sealed interfaces for event types, and proper aggregate encapsulation.

## Expected Output
- File: `domain/entity/Order.java`, `domain/entity/OrderLine.java`, `domain/event/OrderPlacedEvent.java`, `domain/event/DomainEvent.java`, `domain/port/EventPublisher.java`, `domain/port/OrderRepository.java`, `domain/usecase/PlaceOrderUseCase.java`
- Must contain: Order aggregate with OrderLine list, domain events, EventPublisher port, PlaceOrderUseCase publishing events after save
- Must not contain: Framework event classes in domain, `@EventListener` in domain, direct repository calls from event handler

## Scoring Criteria
- [ ] SRP: Order aggregate, lines, events, use case each separate (10 points)
- [ ] Naming: Descriptive names throughout (10 points)
- [ ] Type safety: BigDecimal, sealed interfaces, generics (15 points)
- [ ] 2-layer: Proper aggregate root and domain events (25 points)
- [ ] Domain purity: Zero framework imports (20 points)
- [ ] Events: Proper event publishing, no direct repo calls from handlers (20 points)
