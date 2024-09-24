from decimal import Decimal
import pytest
from my_calculator.single_calculation import ArithmeticOperation
from my_calculator.arithmetic import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

@pytest.mark.parametrize("x, y, operation, result", [
    (Decimal('10'), Decimal('5'), add_numbers, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract_numbers, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply_numbers, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide_numbers, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add_numbers, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract_numbers, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply_numbers, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide_numbers, Decimal('20')),
])
def test_operations(x, y, operation, result):
    """Ensure operations in the ArithmeticOperation class work correctly."""
    calc = ArithmeticOperation(x, y, operation)
    assert calc.execute() == result, f"Failed {operation.__name__} operation with {x} and {y}"

def test_representation():
    """Test the string representation of an ArithmeticOperation instance."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), add_numbers)
    assert repr(operation) == "ArithmeticOperation(10, 5, add_numbers)"

def test_divide_zero():
    """Ensure division by zero raises an error."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc = ArithmeticOperation(Decimal('10'), Decimal('0'), divide_numbers)
        calc.execute()
