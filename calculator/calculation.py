from decimal import Decimal
from typing import Callable
import time

class ArithmeticOperation:
    def __init__(self, operand1: Decimal, operand2: Decimal, operator: Callable[[Decimal, Decimal], Decimal]):
        """Initialize the operation with two operands and an operator."""
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.timestamp = time.time()  # Track when the calculation was made

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
        """Custom string representation to show more details."""
        return f"Operation({self.operand1}, {self.operand2}, {self.operator.__name__}, Performed at: {time.ctime(self.timestamp)})"
