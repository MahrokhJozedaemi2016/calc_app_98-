from calculator.calculations import CalculationManager
from calculator.operations import add, subtract, multiply, divide  # Updated imports
from calculator.calculation import ArithmeticOperation  # Updated import
from decimal import Decimal
from typing import Callable

class MyCalculator:
    @staticmethod
    def perform_operation(a: Decimal, b: Decimal, operator: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Perform a calculation using a static method."""
        operation = ArithmeticOperation(a, b, operator)
        CalculationManager.store(operation)
        return operation.execute()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform addition."""
        return MyCalculator.perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform subtraction."""
        return MyCalculator.perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform multiplication."""
        return MyCalculator.perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform division."""
        return MyCalculator.perform_operation(a, b, divide)

