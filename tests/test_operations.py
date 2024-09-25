"""
This module contains tests for the ArithmeticOperation class and related functions.
"""
from decimal import Decimal
import pytest
from calculator.calculation import ArithmeticOperation  # Changed to import from 'calculator'
from calculator.operations import add, subtract, multiply, divide, power  # Added 'power'

def test_add_operation():
    """Test the addition operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), add)
    assert operation.execute() == Decimal('15')

def test_subtract_operation():
    """Test the subtraction operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), subtract)
    assert operation.execute() == Decimal('5')

def test_multiply_operation():
    """Test the multiplication operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), multiply)
    assert operation.execute() == Decimal('50')

def test_divide_operation():
    """Test the division operation."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), divide)
    assert operation.execute() == Decimal('2')

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
