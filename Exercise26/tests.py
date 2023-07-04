import unittest
from RemoveDuplicatesfromSortedArray_26 import *


class test26(unittest.TestCase):
    def test_one(self):
        lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 23]
        exp_lst = [1,2,3,4,23]
        k = removeDuplicates(lst)

        self.assertEqual(k, len(exp_lst), 'Wrong k')
        for i in range(k):
            self.assertEqual(lst[i], exp_lst[i], 'Wrong nums')
    def test_two(self):
        lst = [1, 1, 2]
        exp_lst = [1,2]
        k = removeDuplicates(lst)

        self.assertEqual(k, len(exp_lst), 'Wrong k')
        for i in range(k):
            self.assertEqual(lst[i], exp_lst[i], 'Wrong nums')


if __name__ == '__main__':
    unittest.main()
