import unittest
from Core import *


class TestUM(unittest.TestCase):
    def set_up(self):
        pass

    def tearDown(self):
        pass

    def test_array_slice(self):
        """If number of slices mod len(list_) = 0"""
        list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list_2 = slice_list(list_, 5)
        for i in [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]:
            self.assertIn(i, list_2)

    def test_array_slice_2(self):
        """If number of slices mod len(list_) is not  0"""
        list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list_3 = slice_list(list_, 3)
        for i in [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]:
            self.assertIn(i, list_3)


if __name__ == '__main__':
    unittest.main()
