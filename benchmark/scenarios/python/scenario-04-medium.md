# Scenario: Library Book Rental System

## Difficulty
Medium

## Description
Implement a library rental system with late fees, reservations, stock management, and date arithmetic.

## Prompt
Create Book and Rental aggregates. Implement rental checkout with due date calculation (14 days), return processing with late fee calculation ($1/day), reservation system with queue, and stock availability checking. Create a ReservationPolicy for different book types (regular, reference, new arrival). Use Decimal for fees, datetime with timezone for dates. Domain must be pure Python.

## Expected Output
- File: `domain/entity/book.py`, `domain/entity/rental.py`, `domain/policy/reservation_policy.py`, `domain/port/*repository.py`, `domain/usecase/*.py`, `infrastructure/rest/*.py`
- Must contain: Book aggregate, Rental with due date, late fee calculation, reservation queue, policy for book types, Decimal for fees
- Must not contain: FastAPI/SQLAlchemy in domain, `float` for money, naive datetime

## Scoring Criteria
- [ ] SRP: Checkout, return, reservation, fee calc each separate (15 points)
- [ ] Naming: Descriptive names (10 points)
- [ ] Type safety: Decimal, datetime with tz, Optional (15 points)
- [ ] 2-layer: Policy pattern, multiple aggregates (20 points)
- [ ] Domain purity: Zero framework imports (20 points)
- [ ] Dates: Timezone-aware datetime, proper date arithmetic (20 points)
