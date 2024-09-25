import time
from typing import List
from calculator.calculation import ArithmeticOperation

class CalculationManager:
    history: List[ArithmeticOperation] = []

    @classmethod
    def store(cls, operation: ArithmeticOperation):
        """Store a new operation in the history."""
        cls.history.append(operation)

    @classmethod
    def clear_history(cls):
        """Clear the history of operations."""
        cls.history.clear()

    @classmethod
    def retrieve_history(cls) -> List[ArithmeticOperation]:
        """Retrieve the entire history of operations."""
        return cls.history

    @classmethod
    def get_last(cls) -> ArithmeticOperation:
        """Retrieve the most recent operation from history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operator(cls, operator_name: str) -> List[ArithmeticOperation]:
        """Find all operations by operator name."""
        return [op for op in cls.history if op.operator.__name__ == operator_name]

    @classmethod
    def retrieve_recent(cls, timeframe: float) -> List[ArithmeticOperation]:
        """Retrieve calculations made within a recent timeframe (in seconds)."""
        current_time = time.time()
        return [op for op in cls.history if hasattr(op, 'timestamp') and current_time - op.timestamp <= timeframe]