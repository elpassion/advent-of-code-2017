import unittest
import numpy as np


def calculate_checksum():
    input = np.loadtxt("input.txt", dtype='i', delimiter='\t')
    rowCheksums = []
    for row in input:
        rowCheksums.append(max(row) - min(row))
    matrixChecksum = sum(rowCheksums)
    return matrixChecksum


class Task01Test(unittest.TestCase):

    def testA(self):
        matrixChecksum = calculate_checksum()
        print(matrixChecksum)


if __name__ == '__main__':
    unittest.main()
