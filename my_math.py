def _gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):

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

def fibonacci(n):
      if not isinstance(n, int):
          raise ValueError("fibonacci() requires an integer")
      
      if n < 0:
          raise ValueError("fibonacci() cannot be negative")
      
      if n == 0:
          return 0
      
      if n == 1:
          return 1
      
      a, b = 0, 1
      for _ in range(2, n + 1):
          a, b = b, a + b
      return b
      

def mean(numbers):
    if not isinstance(numbers, (list, tuple)):
        raise ValueError("mean() requires a list or tuple")

    if len(numbers) == 0:
        raise ValueError("mean() cannot be computed on an empty list")
    
    total = 0
    count = 0
    
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("mean() list must contain numbers only")
    total += n
    count += 1

    return total / count
    