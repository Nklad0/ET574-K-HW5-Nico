from typing import Iterable

def _lcm_two(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a

def lcm(*args: int) -> int:
    if len(args) == 0:
        raise ValueError("lcm() requires at least ONE argument")
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        items = tuple(args[0])
    else:
        items = args

    if len(items) == 0:
        raise ValueError("lcm() requires at least ONE integer")
    
    current_lcm = None
    for x in items:
        if not isinstance(x, int):
            raise ValueError(f"lcm() only accepts integers; got {type(x)}")
        if current_lcm is None:
            current_lcm = abs(x)
        else:
            current_lcm = _lcm_two(current_lcm, x)
        return current_lcm if current_lcm is not None else 0

def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("fibonacci() requires an integer input")
    if n < 0:
        raise ValueError("fibonacci() isn't defined for negative indices")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def mean(numbers: Iterable[float]) -> float:
    if not isinstance(numbers, Iterable):
        raise ValueError("mean() requires an iterable of numbers")
    total = 0.0
    count = 0
    for x in numbers:
        if not isinstance(x, (int, float)):
            raise ValueError("mean() iterable must contain ONLY numbers")
        total += x
        count += 1
    if count == 0:
        raise ValueError("mean() of empty iterable is undefined")
    return total / count