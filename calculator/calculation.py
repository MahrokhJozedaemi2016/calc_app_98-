from decimal import Decimal
from typing import Callable

class ArithmeticOperation:
    def __init__(self, operand1: Decimal, operand2: Decimal, operator: Callable[[Decimal, Decimal], Decimal]):
        """Initialize the operation with two operands and an operator."""
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    @staticmethod
    def initialize(a: Decimal, b: Decimal, operator: Callable[[Decimal, Decimal], Decimal]):
        """Factory method for easier creation."""
        return ArithmeticOperation(a, b, operator)

    def execute(self) -> Decimal:
        """Perform the stored operation."""
        try:
            result = self.operator(self.operand1, self.operand2)
            return result
        except Exception as e:
            print(f"Error in operation: {str(e)}")
            raise e  # You can log or add custom behavior here

    def __repr__(self):
        """Simplified string representation to match the test expectation."""
        return f"ArithmeticOperation({self.operand1}, {self.operand2}, {self.operator.__name__})"