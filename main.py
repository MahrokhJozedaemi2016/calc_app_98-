import sys
from decimal import Decimal, InvalidOperation
from calculator.calculation import ArithmeticOperation  # Import your ArithmeticOperation class
from calculator.operations import add, subtract, multiply, divide  # Import operation functions

def calculate_and_print(a, b, operation_name):
    # Map operation names to actual function references
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Unified error handling for decimal conversion
    try:
        # Convert input values to Decimal
        a_decimal, b_decimal = map(Decimal, [a, b])

        # Retrieve the operation function from the mapping
        operation_function = operation_mappings.get(operation_name)

        if operation_function:
            # Create an ArithmeticOperation instance and execute it
            operation_instance = ArithmeticOperation(a_decimal, b_decimal, operation_function)
            result = operation_instance.execute()

            # Print the result
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            # Handle unknown operation case
            print(f"Unknown operation: {operation_name}")

    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    # Expect exactly three arguments for the calculation
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    # Parse command-line arguments
    _, a, b, operation = sys.argv

    # Call the function to perform the calculation and print the result
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()