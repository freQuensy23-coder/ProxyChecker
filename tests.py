import unittest
from Core import *
from Checker import Checker
import threading


class TestUM(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def tearDown(self):
        pass

    def test_generate_threads(self):
        t_list = generate_threads(proxies=[], checker=self.checker, goods=[])
        for el in t_list:
            self.assertEqual(type(el), threading.Thread)

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

    def test_array_slice_to_short(self):
        """Waiting for raising index error if try to divide short array """
        list_ = [1]
        try:
            self.assertRaises(slice_list(list_, 2), expected_exception=IndexError)
        except IndexError:
            pass


if __name__ == '__main__':
    unittest.main()
