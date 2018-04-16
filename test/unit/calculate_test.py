#! /usr/bin/env python
import unittest
from app.calculate import Calculator


class TestCalulate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_assert_raisaes(self):
        with self.assertRaises(AttributeError):
            [].get

    def test_something(self):
        self.assertTrue('jubii', msg="test")


if __name__ == '__main__':
    unittest.main()
