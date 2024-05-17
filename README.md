# Software Design Patterns Examples

This repository contains Python scripts demonstrating various software design patterns. Each script is a standalone example of a specific design pattern.

## Patterns Covered

- **Abstract Factory**: `AbstractFactory.py`
  - Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

- **Adapter**: `Adapter.py`
  - Allows objects with incompatible interfaces to collaborate.

- **Command**: `Command.py`
  - Encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, and support for undoable operations.

- **Composite**: `Composite.py`
  - Composes objects into tree structures to represent part-whole hierarchies. This lets clients treat individual objects and compositions uniformly.

- **DRY-KISS-YAGNI-SOLID (DKYS)**: `DKYS.py`
  - Placeholder pattern for future implementation or to demonstrate a strategy pattern with a unique twist.

- **Facade**: `Facade.py`
  - Provides a simplified interface to a large body of code or a complex subsystem.

- **Factory Method**: `FactoryMethod.py`
  - Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

- **Object Pool**: `ObjectPool.py`
  - Offers a pool of ready-to-use objects from a fixed set instead of expensive acquisition and release.

- **Prototype**: `Prototype.py`
  - Creates new objects by cloning existing ones.

- **Strategy Pattern**: `Strategy Pattern.py`
  - Enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.

## Usage

To run any script, simply navigate to this directory in your terminal and run:

```bash
python <script_name.py>
