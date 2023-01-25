# Codewars 'Data Reverse' 6 kuy
# A stream of data is received and needs to be reversed.
# # Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 11111111  00000000  00001111  10101010 should become: 10101010  00001111  00000000  11111111
# The total number of bits will always be a multiple of 8.
# The data is given in an array as such: # [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


import unittest
import numpy as np


def data_reverse(data: list) -> list:
    arr = np.array(data).reshape(len(data) // 8, 8)
    arr = np.flipud(arr)
    result = []
    for line in arr:
        result += list(line)
    return result  # might as well just return arr_reversed.flatten().tolist() but mypy complains about type mismatch


class TestDataReverse(unittest.TestCase):
    def test_data_reverse(self):
        data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
        data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(data_reverse(data1), data2)

        data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
        data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
        self.assertEqual(data_reverse(data3), data4)


if __name__ == '__main__':
    unittest.main()
