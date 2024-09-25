"""
This module contains tests for the ArithmeticOperation class and related functions.
"""
from decimal import Decimal
import pytest
from calculator.calculation import ArithmeticOperation  # Import from 'calculator'
from calculator.operations import add, subtract, multiply, divide  # Import from 'calculator'


@pytest.mark.parametrize("operand1, operand2, operation, result", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_operations(operand1, operand2, operation, result):
    """Ensure operations in the ArithmeticOperation class work correctly."""
    calc = ArithmeticOperation(operand1, operand2, operation)
    assert calc.execute() == result, f"Failed {operation.__name__} operation with {operand1} and {operand2}"


def test_representation():
    """Test the string representation of an ArithmeticOperation instance."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), add)
    assert repr(operation) == "ArithmeticOperation(10, 5, add)"


def test_divide_zero():
    """Ensure division by zero raises an error."""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc = ArithmeticOperation(Decimal('10'), Decimal('0'), divide)
        calc.execute()


def test_invalid_operator():
    """Test that an invalid operator raises an exception."""
    # Pass an invalid operator (None) to trigger an exception
    with pytest.raises(TypeError):
        operation = ArithmeticOperation(Decimal('10'), Decimal('5'), None)
        operation.execute()


def test_invalid_operand():
    """Test that an invalid operand raises an exception."""
    with pytest.raises(TypeError):
        operation = ArithmeticOperation("invalid", Decimal('5'), add)
        operation.execute()


def test_catch_all_exception():
    """Test the catch-all exception block in ArithmeticOperation's execute method."""
    # Mock an operator that raises a specific error (e.g., RuntimeError)
    def invalid_operation(operand1, operand2):
        raise RuntimeError("Custom error")  # Use RuntimeError instead of Exception

    with pytest.raises(RuntimeError, match="Custom error"):  # Use RuntimeError here as well
        operation = ArithmeticOperation(Decimal('10'), Decimal('5'), invalid_operation)
        operation.execute()


def test_initialization():
    """Test the initialization of ArithmeticOperation with given operands and operator."""
    operation = ArithmeticOperation(Decimal('10'), Decimal('5'), add)
    # Check if the operands and operator are properly initialized
    assert operation.operand1 == Decimal('10')
    assert operation.operand2 == Decimal('5')
    assert operation.operator == add  # pylint: disable=comparison-with-callable


def test_initialization_via_factory_method():
    """Test the initialization of ArithmeticOperation using the factory method."""
    operation = ArithmeticOperation.initialize(Decimal('10'), Decimal('5'), add)
    assert operation.operand1 == Decimal('10')
    assert operation.operand2 == Decimal('5')
    assert operation.operator is add  # Use "is" for function comparison
