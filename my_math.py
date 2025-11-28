def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    """
    Return the least common multiple of two or more integers.
    Accepts either:
        - lcm(a, b, c, ...)
        - lcm([a, b, c, ...])
    """
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        nums = args[0]
    else:
        nums = args

    if len(nums) == 0:
        raise ValueError("lcm() requires at least one integer")
    
    for n in nums:
        if not isinstance(n, int):
            raise ValueError("lcm() only accepts integers")

    def lcm_two(a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // _gcd(a, b)

    result = nums[0]
    for n in nums[1:]:
        result = lcm_two(result, n)

    return result