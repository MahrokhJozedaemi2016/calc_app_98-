"""
This module contains tests for the main application functionality,
including various arithmetic operations and error handling scenarios.
"""
import sys
import pytest
from main import calculate_and_print, main

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'addition', "The result of 5 addition 3 is equal to 8"),
    ("10", "2", 'subtraction', "The result of 10 subtraction 2 is equal to 8"),
    ("4", "5", 'multiplication', "The result of 4 multiplication 5 is equal to 20"),
    ("20", "4", 'division', "The result of 20 division 4 is equal to 5"),
    ("1", "0", 'division', "An unexpected error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'addition', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtraction', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function with various inputs and operations.

    Parameters:
    a_string (str): The first operand as a string.
    b_string (str): The second operand as a string.
    operation_string (str): The operation to perform.
    expected_string (str): The expected result.
    capsys: Pytest fixture to capture standard output.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string


def test_generic_exception(monkeypatch, capsys):
    """
    Test that a generic exception is caught and handled.
    """
    def mock_decimal(value):
        raise ValueError("Unexpected error")  # Use a more specific exception type

    # Apply the monkeypatch to mock Decimal
    monkeypatch.setattr("main.Decimal", mock_decimal)

    # Run the calculate_and_print function which should trigger the mocked exception
    calculate_and_print("10", "5", "addition")
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Unexpected error" in captured.out.strip()


def test_main_with_missing_arguments(monkeypatch, capsys):
    """
    Test the main function with missing arguments.
    """
    # Simulate passing fewer arguments than expected
    monkeypatch.setattr(sys, 'argv', ['main.py', '5'])
    with pytest.raises(SystemExit):  # Expecting a system exit due to invalid arguments
        main()
    captured = capsys.readouterr()
    assert "Usage: python main.py <number1> <number2> <operation>" in captured.out


def test_main_with_valid_arguments(monkeypatch, capsys):
    """
    Test the main function with valid arguments.
    """
    # Simulate valid arguments
    monkeypatch.setattr(sys, 'argv', ['main.py', '5', '3', 'addition'])
    main()
    captured = capsys.readouterr()
    assert "The result of 5 addition 3 is equal to 8" in captured.out


def test_main_divide_by_zero(monkeypatch, capsys):
    """
    Test division by zero using main function.
    """
    # Simulate arguments for division by zero
    monkeypatch.setattr(sys, 'argv', ['main.py', '1', '0', 'division'])
    main()
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Cannot divide by zero" in captured.out
