# Name: Nico Kladopoulos
# QCC ID: 24688386
# ET574 Homework 5 - Math Functions

import unittest
from my_math import lcm, fibonacci, mean

class TestMyMath(unittest.TestCase):
  def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(3, 5, 10) == 30
    assert lcm(0, 10) == 0

    try:
        lcm(3, 2)
        raise AssertionError("Expected ValueError for a non-integer")
    except ValueError:
        pass


def test_fibonacci_basic(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(6), 8)
    self.assertEqual(fibonacci(10), 55)

def test_fibonacci_bad_inputs(self):
        
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(-3)   
     

def test_mean_basic(self):
        self.assertAlmostEqual(mean([1, 2, 3]), 2.0)
        self.assertAlmostEqual(mean([10, 20]), 15)

def test_mean_errors(self):
        
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean([])
       
        with self.assertRaises((TypeError, ValueError)):
            mean([1, "x", 3]) 


if __name__ == "__main__":
      unittest.main(verbosity=2)
      print("Test sucessfully passed!")
 

