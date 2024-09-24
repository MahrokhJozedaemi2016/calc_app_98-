from typing import List
from my_calculator.single_calculation import ArithmeticOperation

class CalculationManager:
    history: List[ArithmeticOperation] = []

    @classmethod
    def store(cls, operation: ArithmeticOperation):
        """Store a new operation in the history."""
        cls.history.append(operation)

    @classmethod
    def retrieve_history(cls) -> List[ArithmeticOperation]:
        """Retrieve the full history."""
        return cls.history

    @classmethod
    def retrieve_by_operation(cls, operator_name: str) -> List[ArithmeticOperation]:
        """Retrieve history filtered by operator name."""
        return [op for op in cls.history if op.operator.__name__ == operator_name]

    @classmethod
    def retrieve_recent(cls, timeframe: float) -> List[ArithmeticOperation]:
        """Retrieve calculations made within a recent timeframe (in seconds)."""
        current_time = time.time()
        return [op for op in cls.history if current_time - op.timestamp <= timeframe]
