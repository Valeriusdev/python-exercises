from typing import Iterator, Iterable

def modifier(i:int) -> int:
    return i + 10

def my_map(array: Iterable, modifier: callable) -> Iterator:
    return (modifier(item) for item in array)


if __name__ == "__main__":
    array = iter([ 4, 2, 7, 8, 1])    
    result = my_map(array, modifier)
    print(*result)    
