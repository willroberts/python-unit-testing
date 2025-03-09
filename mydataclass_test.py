import unittest
from mydataclass import MyDataClass


class TestMyDataClass(unittest.TestCase):
    def test_init(self):
        d = MyDataClass('foo', 42)
        self.assertEqual(d.name, 'foo')
        self.assertEqual(d.value, 42)
        result = d.add(-42)
        self.assertEqual(result, 0)
        self.assertEqual(d.value, 0)

if __name__ == '__main__':
    unittest.main()
