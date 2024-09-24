from my_calculator.calculation_handler import CalculationManager
from my_calculator.arithmetic import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from my_calculator.single_calculation import ArithmeticOperation
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
        return MyCalculator.perform_operation(a, b, add_numbers)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform subtraction."""
        return MyCalculator.perform_operation(a, b, subtract_numbers)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform multiplication."""
        return MyCalculator.perform_operation(a, b, multiply_numbers)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Static method to perform division."""
        return MyCalculator.perform_operation(a, b, divide_numbers)

