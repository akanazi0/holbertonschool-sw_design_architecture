#!/usr/bin/env python3
"""Factory Pattern using a dynamic registry.

Extending the factory without modifying its core creation logic.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    @abstractmethod
    def mode(self) -> str:
        """Return the mode of travel."""
        pass


class Bus(Vehicle):
    """Bus concrete vehicle."""

    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    """Train concrete vehicle."""

    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    """Bike concrete vehicle."""

    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    """Scooter concrete vehicle."""

    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """Factory that creates vehicles using a registry."""

    def __init__(self) -> None:
        self._registry: dict[str, type[Vehicle]] = {}

    def register_kind(self, kind: str, cls: type[Vehicle]) -> None:
        """Register a vehicle class under a string key."""
        self._registry[kind] = cls

    def create(self, kind: str) -> Vehicle:
        """Create and return an instance of the requested vehicle kind."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main() -> None:
    factory = VehicleFactory()

    # Pre-registered types
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    # Register the new type without modifying VehicleFactory.create
    factory.register_kind("scooter", Scooter)

    # Output verification
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
