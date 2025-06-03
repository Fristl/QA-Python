"""First file with using linters."""
from __future__ import annotations


def calculate_average(nums: list[int | float]) -> float:
    """Calculate the average between numbers."""
    total = sum(nums)
    count = len(nums)
    return total / count


nums: list[int | float] = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)  # noqa: T201
