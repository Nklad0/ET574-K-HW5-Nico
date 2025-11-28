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

