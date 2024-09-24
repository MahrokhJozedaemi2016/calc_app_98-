from decimal import Decimal
import pytest
from my_calculator.single_calculation import ArithmeticOperation
from my_calculator.calculation_handler import CalculationManager
from my_calculator.arithmetic import add_numbers, subtract_numbers

@pytest.fixture
def setup_history():
    """Clear history and add sample calculations for testing."""
    CalculationManager.clear_history()
    CalculationManager.store(ArithmeticOperation(Decimal('10'), Decimal('5'), add_numbers))
    CalculationManager.store(ArithmeticOperation(Decimal('20'), Decimal('3'), subtract_numbers))

def test_add_history(setup_history):
    """Test adding a new calculation to the history."""
    calc = ArithmeticOperation(Decimal('2'), Decimal('2'), add_numbers)
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
    additions = CalculationManager.find_by_operator("add_numbers")
    subtractions = CalculationManager.find_by_operator("subtract_numbers")
    assert len(additions) == 1
    assert len(subtractions) == 1

def test_latest_empty_history():
    """Test getting the latest calculation when the history is empty."""
    CalculationManager.clear_history()
    assert CalculationManager.get_last() is None
