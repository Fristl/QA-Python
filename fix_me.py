"""First file with using linters."""
from __future__ import annotations


def calculate_average(nums: list[int | float]) -> float:
    """Calculate the average between list of numbers."""
    total = sum(nums)
    count = len(nums)
    return total / count


numbers: list[int | float] = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)  # noqa: T201
