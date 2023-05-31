"""
Fib(N) -> Nth fib number
fib(n) == (fib(n) - 1) + (fib(n) - 2)
1, 2, 3, 4, 5, 6
1, 1, 2, 3, 5, 8
"""

# def fib(n):
#     if n <= 1:
#         return n    
#     return fib(n-1) + fib(n-2)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        # temp = a + b  
        # a = b
        # b = temp                          
    return a


if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
