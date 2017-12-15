import unittest


class Task01Test(unittest.TestCase):

    def testA(self):
        map = method_name()
        self.assertEqual(1, map[(0, 0)])
        self.assertEqual(1, map[(1, 0)])
        self.assertEqual(2, map[(1, 1)])
        self.assertEqual(4, map[(0, 1)])


if __name__ == '__main__':
    unittest.main()


def method_name():
    a = dict()
    for i in range(-100, 100):
        for j in range(-100, 100):
            a[(i, j)] = 0

    a[(0, 0)] = 1
    a[(1, 0)] = 1
    w = 1
    h = 1
    n = 2
    while True:
        x = 0
        y = 0

        for yr in range(0, n):
            print(yr)
            a[(x + w, yr)] = sum_of_neighbours(a, x + w, yr)

        for xt in range(0, n):
            print(n - 1 - xt, y + h)
            a[(n - 1 - xt, y + h)] = sum_of_neighbours(a, n - 1 - xt, y + h)

        # for yl in range(0, n):
        #     a[(x - w, n - yl)] = sum_of_neighbours(a, x - w, n - yl)
        #
        # for xb in range(0, n + 1):
        #     a[(xb, y - h)] = sum_of_neighbours(a, xb, y - h)
        h += 1
        n += 1
        w += 1
        # 1, 0
        # 1, 1
        # 0, 1
        # -1, 1
        # -1, 0
        # -1, -1
        #

        break
    return a


def sum_of_neighbours(a, x, y):
    return a[(x - 1, y)] + a[(x + 1, y)] + a[(x, y - 1)] + a[(x, y + 1)] + a[(x - 1, y - 1)] + a[(x + 1, y + 1)]
