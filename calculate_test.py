#! /usr/bin/env python
import unittest
from calculate import Calculator


class TestCalulate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))


if __name__ == '__main__':
    unittest.main()
