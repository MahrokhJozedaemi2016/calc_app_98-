from my_calculator.calculation_handler import CalculationManager
from my_calculator.arithmetic import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from my_calculator.single_calculation import ArithmeticOperation
from decimal import Decimal

class MyCalculator:
    def __init__(self):
        """Initialize with an empty state or any necessary attributes."""
        self.state = {}

    def perform_operation(self, a: Decimal, b: Decimal, operator) -> Decimal:
        """Perform the arithmetic operation and store result."""
        operation = ArithmeticOperation(a, b, operator)
        CalculationManager.store(operation)
        return operation.execute()

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        """Instance method to perform addition."""
        return self.perform_operation(a, b, add_numbers)

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        """Instance method to perform subtraction."""
        return self.perform_operation(a, b, subtract_numbers)

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        """Instance method to perform multiplication."""
        return self.perform_operation(a, b, multiply_numbers)

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        """Instance method to perform division with zero-checking."""
        return self.perform_operation(a, b, divide_numbers)

