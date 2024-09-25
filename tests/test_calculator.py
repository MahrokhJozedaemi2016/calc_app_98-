"""
This module contains tests for the ArithmeticOperation class and related functions.
"""
from calculator import MyCalculator  # Changed to import from 'calculator'

def test_add():
    """Test addition functionality."""
    assert MyCalculator.add(2, 3) == 5

def test_subtract():
    """Test subtraction functionality."""
    assert MyCalculator.subtract(5, 2) == 3

def test_multiply():
    """Test multiplication functionality."""
    assert MyCalculator.multiply(3, 3) == 9

def test_divide():
    """Test division functionality."""
    assert MyCalculator.divide(10, 2) == 5
