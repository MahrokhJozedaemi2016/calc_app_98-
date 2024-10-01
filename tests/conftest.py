"""
This module provides pytest fixtures and test data generation for arithmetic operations
used in the calculator application.
"""

from decimal import Decimal
from faker import Faker
from calculator.operations import addition, subtraction, multiplication, division  # Renamed operations

fake = Faker()

def generate_test_data(num_records):
    """
    Generates random test data for arithmetic operations.

    Parameters:
    num_records (int): The number of test records to generate.

    Yields:
    tuple: A tuple containing operand1, operand2, the operation, and the expected result.
    """
    operation_mappings = {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division
    }

    for _ in range(num_records):
        operand1 = Decimal(fake.random_number(digits=2))
        operand2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure operand2 is not zero for division operation to prevent division by zero
        if operation_func.__name__ == 'division':
            operand2 = Decimal('1') if operand2 == Decimal('0') else operand2

        try:
            # Perform the operation
            expected = operation_func(operand1, operand2)
        except ZeroDivisionError:
            # Handle division by zero
            expected = "ZeroDivisionError"

        # Yield the test data as a tuple
        yield operand1, operand2, operation_func, expected


def pytest_addoption(parser):
    """
    Adds a command-line option to specify the number of test records.

    Parameters:
    parser: The pytest command-line parser.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")


def pytest_generate_tests(metafunc):
    """
    Generates parameterized test cases using the test data.

    Parameters:
    metafunc: The test function that will be parameterized.
    """
    if {"operand1", "operand2", "expected"}.intersection(set(metafunc.fixturenames)):
        # Get the number of test records from the command-line option
        num_records = metafunc.config.getoption("num_records")
        # Generate test data
        parameters = list(generate_test_data(num_records))
        # Parametrize the test function with the generated data
        metafunc.parametrize("operand1, operand2, operation, expected", parameters)
