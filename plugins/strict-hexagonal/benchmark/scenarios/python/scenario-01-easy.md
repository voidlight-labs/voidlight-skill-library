# Scenario: Temperature Converter Service

## Difficulty
Easy

## Description
Implement a temperature conversion service with enums, dataclasses, and 2-layer architecture using FastAPI.

## Prompt
Create a TemperatureUnit enum (Celsius, Fahrenheit, Kelvin), a Temperature dataclass with value and unit, and 6 conversion functions (each unit to each other). Implement a TemperatureConverterUseCase and a FastAPI endpoint in infrastructure. Use Decimal for precision, type hints everywhere, and ensure domain has zero FastAPI imports.

## Expected Output
- File: `domain/entity/temperature.py`, `domain/usecase/convert_temperature.py`, `infrastructure/rest/temperature_controller.py`
- Must contain: TemperatureUnit enum, Temperature dataclass, 6 pure conversion functions, use case, FastAPI endpoint
- Must not contain: `Any` type, `float` for temperature values, FastAPI imports in domain

## Scoring Criteria
- [ ] SRP: Each conversion is a separate function (15 points)
- [ ] Naming: Descriptive function names (10 points)
- [ ] Type safety: Decimal, type hints, enum (15 points)
- [ ] 2-layer: Domain pure, infra has FastAPI (25 points)
- [ ] Domain purity: Zero FastAPI/Pydantic imports in domain (20 points)
- [ ] Functions: 6 separate conversion functions, each single responsibility (15 points)
