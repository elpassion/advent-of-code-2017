import unittest


class Task02Test(unittest.TestCase):

    def test_spriale_matrix(self):
        map = create_spiral_sum_matrix(325489)
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
        self.assertEqual(147, map[(-2, 2)])


if __name__ == '__main__':
    unittest.main()


def create_spiral_sum_matrix(until):
    matrix = dict()
    fill_matrix_with_zeros(matrix)

    matrix[(0, 0)] = 1
    depth = 1
    while True:
        finish = False
        for yr in range(0, depth + 1):
            sum = sum_of_neighbours(matrix, depth, yr)
            if sum > until:
                print(sum)
                finish = True
            matrix[(depth, yr)] = sum

        for xt in range(0, depth + 2):
            sum = sum_of_neighbours(matrix, depth - xt, depth)
            if sum > until:
                print(sum)
                finish = True
            matrix[(depth - xt,depth)] = sum

        for yl in range(0, depth + 2):
            sum = sum_of_neighbours(matrix, - depth, depth - yl)
            if sum > until:
                print(sum)
                finish = True
            matrix[(- depth, depth - yl)] = sum

        for xb in range(0, depth + 2):
            sum = sum_of_neighbours(matrix, xb, - depth)
            if sum > until:
                print(sum)
                finish = True
            matrix[(xb, - depth)] = sum

        depth += 1
        if finish:
            break
    return matrix


def fill_matrix_with_zeros(a):
    for i in range(-10, 10):
        for j in range(-10, 10):
            a[(i, j)] = 0


def sum_of_neighbours(a, x, y):
    return a[(x - 1, y)] + a[(x + 1, y)] + a[(x, y - 1)] + \
           a[(x, y + 1)] + a[(x - 1, y - 1)] + a[(x + 1, y + 1)] + \
           a[(x + 1, y - 1)] + a[(x - 1, y + 1)]
