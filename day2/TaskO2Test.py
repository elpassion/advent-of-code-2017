import unittest
import numpy as np


def calculate_checksum():
    input = np.loadtxt("input.txt", dtype='i', delimiter='\t')
    rowCheksums = []
    for row in input:
        for n_ndx, number in enumerate(row):
            for sn_ndx, s_number in enumerate(row):
                if n_ndx != sn_ndx:
                    divisionResult = number / s_number
                    if divisionResult.is_integer():
                        rowCheksums.append(divisionResult)

    matrixChecksum = sum(rowCheksums)
    return matrixChecksum


class Task01Test(unittest.TestCase):

    def testA(self):
        matrixChecksum = calculate_checksum()
        print(matrixChecksum)


if __name__ == '__main__':
    unittest.main()
