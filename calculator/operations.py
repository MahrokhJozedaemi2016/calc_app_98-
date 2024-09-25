from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Perform addition."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Perform subtraction."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Perform multiplication."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division, with additional validation for zero."""
    if b == Decimal(0):
        raise ValueError("Division by zero is not allowed.")
    return a / b

def power(a: Decimal, b: Decimal) -> Decimal:
    """Perform exponentiation."""
    return a ** b

