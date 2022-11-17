#!/usr/bin/python3

import unittest
from fibonacci import Fibonacci

class TestCase(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(Fibonacci(1), 1)

	def test_case_2(self):
		self.assertEqual(Fibonacci(5), 5)

	def test_case_3(self):
		self.assertEqual(Fibonacci(7), 13)

if __name__ == '__main__':
	unittest.main()