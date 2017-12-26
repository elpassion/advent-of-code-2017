import unittest


class Task01Test(unittest.TestCase):

    def test_count_steps(self):
        with open("input.txt") as f:
            input = f.readlines()
        input = [int(x.strip()) for x in input]
        current = 0
        length = len(input)
        count = 0
        while True:
            current = next_step(input, current)
            count = count + 1
            if current >= length:
                break
        print(count)

    def test_first_step(self):
        input = [0, 3, 0, 1, -3]
        current = 0
        current = next_step(input, current)
        self.assertEqual(0, current)
        self.assertEqual([1, 3, 0, 1, -3], input)

    def test_second_step(self):
        input = [1, 3, 0, 1, -3]
        current = 0
        current = next_step(input, current)
        self.assertEqual(1, current)
        self.assertEqual([2, 3, 0, 1, -3], input)

    def test_third_step(self):
        input = [2, 3, 0, 1, -3]
        current = 1
        current = next_step(input, current)
        self.assertEqual(4, current)
        self.assertEqual([2, 4, 0, 1, -3], input)

    def test_fourth_step(self):
        input = [2, 4, 0, 1, -3]
        current = 4
        current = next_step(input, current)
        self.assertEqual(1, current)
        self.assertEqual([2, 4, 0, 1, -2], input)

    def test_fifth_step(self):
        input = [2, 4, 0, 1, -2]
        current = 1
        current = next_step(input, current)
        self.assertEqual(5, current)
        self.assertEqual([2, 5, 0, 1, -2], input)


if __name__ == '__main__':
    unittest.main()


def next_step(input, current):
    old = current
    current = current + input[current]
    input[old] = input[old] + 1
    return current
