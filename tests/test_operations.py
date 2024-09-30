"""
This module contains tests for the ArithmeticOperation class and related functions.
"""
from decimal import Decimal
import pytest
from calculator.calculation import ArithmeticOperation  # Changed to import from 'calculator'
from calculator.operations import add, subtract, multiply, divide, power  # Added 'power'

def test_operation(operand1, operand2, operation, result):
    """
    Test calculation operations for various scenarios.
    """
    calc = ArithmeticOperation(operand1, operand2, operation)
    assert calc.execute() == result, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """Test the divide by zero exception."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        operation = ArithmeticOperation(Decimal('10'), Decimal('0'), divide)
        operation.execute()

# New test for the power operation to cover line 23 in operations.py
def test_power_operation():
    """Test the power operation."""
    operation = ArithmeticOperation(Decimal('2'), Decimal('3'), power)
    assert operation.execute() == Decimal('8'), "Power operation failed"
