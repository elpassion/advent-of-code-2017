import unittest


class Task02Test(unittest.TestCase):

    def test_spriale_matrix(self):
        map = create_spiral_sum_matrix()
        self.assertEqual(1, map[(0, 0)])
        self.assertEqual(1, map[(1, 0)])
        self.assertEqual(2, map[(1, 1)])
        self.assertEqual(4, map[(0, 1)])
        self.assertEqual(5, map[(-1, 1)])
        self.assertEqual(10, map[(-1, 0)])
        self.assertEqual(11, map[(-1, -1)])
        self.assertEqual(23, map[(0, -1)])
        self.assertEqual(25, map[(1, -1)])
        self.assertEqual(26, map[(2, -1)])
        self.assertEqual(54, map[(2, 0)])
        self.assertEqual(57, map[(2, 1)])


if __name__ == '__main__':
    unittest.main()


def create_spiral_sum_matrix():
    a = dict()
    for i in range(-100, 100):
        for j in range(-100, 100):
            a[(i, j)] = 0

    a[(0, 0)] = 1
    a[(1, 0)] = 1
    depth = 1
    while True:
        for yr in range(0, depth + 1):
            a[(depth, yr)] = sum_of_neighbours(a, depth, yr)

        for xt in range(0, depth + 2):
            a[(depth - xt, + depth)] = sum_of_neighbours(a, depth - xt, depth)

        for yl in range(0, depth + 2):
            a[(- depth, depth - yl)] = sum_of_neighbours(a, - depth, depth - yl)

        for xb in range(0, depth + 2):
            a[(xb, - depth)] = sum_of_neighbours(a, xb, - depth)
        depth += 1
        if depth == 4:
            break
    return a


def sum_of_neighbours(a, x, y):
    return a[(x - 1, y)] + a[(x + 1, y)] + a[(x, y - 1)] +\
           a[(x, y + 1)] + a[(x - 1, y - 1)] + a[(x + 1, y + 1)] + \
           a[(x + 1, y - 1)] + a[(x - 1, y + 1)]
