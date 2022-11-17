#!/usr/bin/python3

import unittest
from fibonacci import Fibonacci

class TestCase(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(Fibonacci(2), 2)

	def test_case_2(self):
		self.assertEqual(Fibonacci(10), 100)

if __name__ == '__main__':
	unittest.main()