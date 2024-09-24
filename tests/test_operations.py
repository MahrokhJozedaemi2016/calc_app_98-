from decimal import Decimal
import pytest
from my_calculator.single_calculation import ArithmeticOperation
from my_calculator.arithmetic import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_operation():
    """Test the addition operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), add_numbers)
    assert operation.execute() == Decimal('15')

def test_subtract_operation():
    """Test the subtraction operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), subtract_numbers)
    assert operation.execute() == Decimal('5')

def test_multiply_operation():
    """Test the multiplication operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), multiply_numbers)
    assert operation.execute() == Decimal('50')

def test_divide_operation():
    """Test the division operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), divide_numbers)
    assert operation.execute() == Decimal('2')

def test_divide_by_zero():
    """Test the divide by zero exception."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        operation = ArithmeticOperation(Decimal('10'), Decimal('0'), divide_numbers)
        operation.execute()

