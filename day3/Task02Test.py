import unittest


class Task02Test(unittest.TestCase):

    def test_spriale_matrix(self):
        map = create_spiral_sum_matrix(lambda x: x > 325489)
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


def create_spiral_sum_matrix(finish_predicate):
    matrix = dict()
    matrix[(0, 0)] = 1
    depth = 1
    while True:
        finish = create_edge(depth, matrix, lambda var: (depth, var - depth), finish_predicate)
        if finish:
            break
        finish = create_edge(depth, matrix, lambda var: (depth - var, depth), finish_predicate)
        if finish:
            break
        finish = create_edge(depth, matrix, lambda var: (- depth, depth - var), finish_predicate)
        if finish:
            break

        cords_creator = lambda var: (var - depth, - depth)
        finish = create_edge(depth, matrix, cords_creator, finish_predicate)

        cords = cords_creator(depth * 2 + 1)
        matrix[cords] = sum_of_neighbours(matrix, cords)

        depth += 1
        if finish:
            break
    return matrix


def create_edge(depth, matrix, cords_creator, predicate):
    finish = False
    for variable in range(1, depth * 2 + 1):
        sum = sum_of_neighbours(matrix, cords_creator(variable))
        if predicate(sum):
            print(sum)
            finish = True
            break
        matrix[cords_creator(variable)] = sum
    return finish


def sum_of_neighbours(a, pair):
    x, y = pair
    return a.get((x - 1, y), 0) + a.get((x + 1, y), 0) + a.get((x, y - 1), 0) + \
           a.get((x, y + 1), 0) + a.get((x - 1, y - 1), 0) + a.get((x + 1, y + 1), 0) + \
           a.get((x + 1, y - 1), 0) + a.get((x - 1, y + 1), 0)
