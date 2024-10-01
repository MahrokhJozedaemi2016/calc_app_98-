"""
This module serves as the entry point for the calculator application. It processes user input from the command line
and performs the requested arithmetic operation.
"""
import sys
from calculator import ArithmeticEngine
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    # Map both old and new operation names
    operation_mappings = {
        'add': ArithmeticEngine.add,
        'addition': ArithmeticEngine.add,
        'subtract': ArithmeticEngine.subtract,
        'subtraction': ArithmeticEngine.subtract,
        'multiply': ArithmeticEngine.multiply,
        'multiplication': ArithmeticEngine.multiply,
        'divide': ArithmeticEngine.divide,
        'division': ArithmeticEngine.divide,
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)  # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()