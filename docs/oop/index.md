# OOP & Design Principles

## Encapsulation / Abstraction

- **Encapsulation**: bundle data + behavior together; hide internal state. Expose only what's needed.
- **Abstraction**: define *what* an object does (interface), hide *how* it does it (implementation).

## Inheritance vs Composition

- **Inheritance** (`is-a`): subclass inherits parent's interface and implementation. Risk: tight coupling, fragile base class problem.
- **Composition** (`has-a`): object contains other objects as fields. More flexible, easier to test.

> Prefer composition over inheritance (GoF principle).

## SOLID

| Letter | Principle | One-liner |
|--------|-----------|-----------|
| S | Single Responsibility | A class should have one reason to change |
| O | Open/Closed | Open for extension, closed for modification |
| L | Liskov Substitution | Subtypes must be substitutable for base types |
| I | Interface Segregation | Many small interfaces > one fat interface |
| D | Dependency Inversion | Depend on abstractions, not concretions |

## Interfaces / Contracts

An interface defines a **contract**: "any class implementing this must provide these methods." Enables polymorphism and dependency injection. Essential for testability.

## Design Patterns

### Factory

Creates objects without exposing instantiation logic. Caller asks for an object by type/name; factory decides which class to instantiate.

```python
class ShapeFactory:
    @staticmethod
    def create(kind: str) -> Shape:
        if kind == "circle": return Circle()
        if kind == "rect": return Rectangle()
        raise ValueError(kind)
```

### Singleton

Ensures only one instance exists. Use sparingly — it's a global state and makes testing harder.

```python
class Config:
    _instance = None

    @classmethod
    def get(cls) -> "Config":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```

### Observer / Strategy / Decorator

- **Observer**: publish/subscribe. Subjects notify registered observers on state change.
- **Strategy**: swap algorithms at runtime via an interface (e.g. sort strategy: bubble, merge).
- **Decorator**: wrap objects to add behavior without subclassing.
