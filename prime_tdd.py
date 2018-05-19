"""
partition inputs:
number(int): -> 0 - infinity
  -> negatives :-> error
  -> small positive :-> 0 1 2 3 4 5
  -> middle postive :-> 20, 30, 50
  -> large numbers :-> 10000, 1000000000

 0, -1 bunadaries
 10000000000000000000, edge case

 {}, "", (,) -> unexpected input
"""

from prime import prime_tdd as prime

import unittest

class TestPrime(unittest.TestCase):
  def test_negative(self, number=-20):
    resluts = prime(number)
    self.assertEqual(resluts, "error")


  def test_small_postive_numbers(self, number=2):
    resluts = prime(number)
    self.assertTrue(resluts == [2])

  def test_middle_positive_numbers(self, number=20):
    results = prime(number)
    self.assertTrue(results == [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
