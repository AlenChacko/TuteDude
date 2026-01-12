# Object-Oriented Programming (OOP) in Python
## Complete Theory Notes | Beginner → Pro

---

## LESSON 1: Introduction to OOP

### What is Object-Oriented Programming?
Object-Oriented Programming (OOP) is a programming paradigm that structures a program using **objects**, which represent real-world entities.

Each object contains:
- **Attributes** → Data / State
- **Methods** → Behavior / Actions

---

### Why OOP?
- Models real-world problems
- Improves code organization
- Enables code reuse
- Makes programs scalable and maintainable
- Widely used in large applications and frameworks

---

### Core Pillars of OOP
1. Class  
2. Object  
3. Encapsulation  
4. Inheritance  
5. Polymorphism  
6. Abstraction  

---

## LESSON 2: Class and Object

### Class
A **class** is a blueprint or template used to create objects.  
It defines what attributes and methods an object will have.

---

### Object
An **object** is an instance of a class.  
It represents a real, usable entity created from the class.

---

### Key Difference
- Class → Blueprint  
- Object → Real instance created from blueprint  

---

## LESSON 3: Attributes and Methods

### Attributes
Attributes are variables that store data inside a class.

Types:
- Instance attributes (unique to each object)
- Class attributes (shared by all objects)

---

### Methods
Methods are functions defined inside a class that describe object behavior.

---

### `self` Keyword
- Refers to the current object
- Used to access object attributes and methods
- Mandatory in instance methods

---

## LESSON 4: Constructor (`__init__`)

### What is a Constructor?
A constructor is a special method that executes automatically when an object is created.

---

### Purpose of Constructor
- Initialize object data
- Assign values at object creation
- Avoid hardcoding values

---

### Characteristics
- Named `__init__`
- Runs only once per object
- Can accept parameters

---

## LESSON 5: Instance Variables vs Class Variables

### Instance Variables
- Belong to an object
- Created using `self`
- Each object has its own copy

---

### Class Variables
- Belong to the class
- Shared across all objects
- Defined outside methods

---

### Comparison

| Feature | Instance Variable | Class Variable |
|------|------------------|---------------|
| Scope | Object-level | Class-level |
| Memory | Separate copy | Single shared copy |
| Access | `self.var` | `Class.var` |

---

## LESSON 6: Types of Methods

### Instance Method
- Uses `self`
- Accesses object data
- Most commonly used

---

### Class Method
- Uses `cls`
- Accesses class-level data
- Defined using `@classmethod`

---

### Static Method
- No `self` or `cls`
- Utility or helper function
- Defined using `@staticmethod`

---

## LESSON 7: Encapsulation

### What is Encapsulation?
Encapsulation is the process of **binding data and methods together** and **restricting direct access to data**.

---

### Benefits
- Protects sensitive data
- Prevents accidental modification
- Improves code security and maintainability

---

### Access Modifiers (Python Convention)

| Modifier | Syntax | Meaning |
|-------|------|--------|
| Public | `var` | Accessible everywhere |
| Protected | `_var` | Intended for internal use |
| Private | `__var` | Name-mangled, restricted |

---

## LESSON 8: Getters and Setters

### Why Getters and Setters?
- Access private data safely
- Add validation logic
- Control data modification

---

### Approaches
1. Traditional getter and setter methods
2. `@property` decorator (Pythonic way)

---

## LESSON 9: Inheritance

### What is Inheritance?
Inheritance allows one class to **reuse the properties and methods of another class**.

---

### Parent Class
Class whose properties are inherited.

---

### Child Class
Class that inherits properties.

---

### Advantages
- Code reuse
- Reduced duplication
- Easier maintenance

---

### Types of Inheritance
1. Single  
2. Multilevel  
3. Multiple  
4. Hierarchical  
5. Hybrid  

---

## LESSON 10: `super()` Keyword

### Purpose
- Access parent class methods or constructor
- Avoid redundant code
- Maintain inheritance hierarchy

---

### Characteristics
- Refers to parent class
- Works with method resolution order (MRO)

---

## LESSON 11: Polymorphism

### What is Polymorphism?
Polymorphism means **one interface, multiple behaviors**.

---

### Forms of Polymorphism
- Method overriding
- Duck typing
- Operator overloading

---

### Method Overriding
Child class provides its own implementation of a parent method.

---

### Duck Typing
Behavior matters more than object type.

---

## LESSON 12: Operator Overloading

### Definition
Operator overloading allows redefining operators (`+`, `-`, `*`, etc.) for user-defined objects.

---

### Purpose
- Improve readability
- Make objects behave like built-in types

---

### Achieved Using
Magic (dunder) methods such as `__add__`, `__sub__`, etc.

---

## LESSON 13: Abstraction

### What is Abstraction?
Abstraction hides internal implementation details and exposes only essential features.

---

### Why Abstraction?
- Enforces structure
- Prevents incomplete implementation
- Improves design clarity

---

### Abstract Class
- Cannot be instantiated
- May contain abstract methods
- Implemented using `abc` module

---

## LESSON 14: Composition vs Inheritance

### Inheritance (IS-A)
Represents an "is-a" relationship.

---

### Composition (HAS-A)
Represents a "has-a" relationship.

---

### Best Practice
Prefer **composition** over inheritance for flexible design.

---

## LESSON 15: Magic (Dunder) Methods

### What are Magic Methods?
Special methods with double underscores used to customize object behavior.

---

### Common Magic Methods

| Method | Purpose |
|------|--------|
| `__init__` | Object creation |
| `__str__` | String representation |
| `__len__` | Length of object |
| `__add__` | Addition operator |

---

## LESSON 16: OOP Design Best Practices

- Use meaningful class names
- One responsibility per class
- Avoid deep inheritance chains
- Encapsulate internal data
- Use abstraction for APIs
- Write clean and readable code

---

## LESSON 17: OOP Concept Summary

- OOP is a design philosophy
- Encourages modular and reusable code
- Essential for large-scale applications
- Backbone of modern Python frameworks

---

## End of OOP Theory Notes
