"""
This module contains tests for the ArithmeticOperation class and related functions.
"""
import time #For testing the retrieve_recent method
from decimal import Decimal #Standard library import
import pytest #third party import
from calculator.calculation import ArithmeticOperation  # Changed to import from 'calculator'
from calculator.calculations import CalculationManager  # No change needed here
from calculator.operations import add, subtract  # Changed to import from 'calculator'

@pytest.fixture
def setup_history():
    """Clear history and add sample calculations for testing."""
    CalculationManager.clear_history()
    CalculationManager.store(ArithmeticOperation(Decimal('10'), Decimal('5'), add))
    CalculationManager.store(ArithmeticOperation(Decimal('20'), Decimal('3'), subtract))

def test_add_history(setup_history):
    """Test adding a new calculation to the history."""
    calc = ArithmeticOperation(Decimal('2'), Decimal('2'), add)
    CalculationManager.store(calc)
    assert CalculationManager.get_last() == calc

def test_retrieve_history(setup_history):
    """Test retrieving the calculation history."""
    assert len(CalculationManager.retrieve_history()) == 2

def test_clear_history(setup_history):
    """Test clearing the calculation history."""
    CalculationManager.clear_history()
    assert len(CalculationManager.retrieve_history()) == 0

def test_latest_calculation(setup_history):
    """Test retrieving the latest calculation."""
    latest = CalculationManager.get_last()
    assert latest.operand1 == Decimal('20') and latest.operand2 == Decimal('3')

def test_find_by_operator(setup_history):
    """Test finding calculations by operation."""
    additions = CalculationManager.find_by_operator("add")
    subtractions = CalculationManager.find_by_operator("subtract")
    assert len(additions) == 1
    assert len(subtractions) == 1

def test_latest_empty_history():
    """Test getting the latest calculation when the history is empty."""
    CalculationManager.clear_history()
    assert CalculationManager.get_last() is None

# New Test for the `retrieve_recent` method to cover lines 37-38 in calculations.py
def test_retrieve_recent_operations():
    """Test that retrieve_recent returns only recent calculations."""
    # Clear the history and add new operations with specific timestamps
    CalculationManager.clear_history()

    # Mocking timestamps for operations
    operation1 = ArithmeticOperation(Decimal('10'), Decimal('5'), add)
    operation1.timestamp = time.time() - 5  # Performed 5 seconds ago
    CalculationManager.store(operation1)

    operation2 = ArithmeticOperation(Decimal('20'), Decimal('3'), subtract)
    operation2.timestamp = time.time() - 60  # Performed 60 seconds ago
    CalculationManager.store(operation2)

    # Retrieve operations made within the last 10 seconds
    recent_operations = CalculationManager.retrieve_recent(10)
    # Assert that only the recent operation (within 10 seconds) is returned
    assert len(recent_operations) == 1
    assert recent_operations[0] == operation1

    # Retrieve operations made within the last 70 seconds
    more_recent_operations = CalculationManager.retrieve_recent(70)
    # Assert that both operations are returned within a 70 second window
    assert len(more_recent_operations) == 2
