#!/usr/bin/env python3.13
import unittest
from myclass import MyClass


class TestMyClass(unittest.TestCase):
    def setUp(self):
        # Use this function to organize test code.
        pass
    def test_init(self):
        c = MyClass(0)
        self.assertEqual(c.value, 0)
    def test_throw(self):
        c = MyClass(0)
        with self.assertRaises(Exception):
            c.throw()
    def tearDown(self):
        # Use this function to clean up test code.
        pass

if __name__ == '__main__':
    unittest.main()
