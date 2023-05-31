"""
Challenge: Find the Maximum Number
Write a Python function that takes a list of numbers as input
and returns the maximum number from the list.
Example:
numbers = [5, 10, 2, 8, 3]
max_number = find_max_number(numbers)
print(max_number)  
Output: 10
"""

from typing import Iterable
from typing import Any

def find_max_number(numbers: Iterable[Any]) -> Any:
    max_num = numbers[0]
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
    return max_num


if __name__ == "__main__":
    numbers = [5, 10, 2, 8, 3]
    print(find_max_number(numbers))
