import unittest


class Task01Test(unittest.TestCase):

    def test_first_cycle(self):
        banks = [0, 2, 7, 0]
        redistribute(banks)
        self.assertEqual([2, 4, 1, 2], banks)

    def test_second_cycle(self):
        banks = [2, 4, 1, 2]
        redistribute(banks)
        self.assertEqual([3, 1, 2, 3], banks)

    def test_third_cycle(self):
        banks = [3, 1, 2, 3]
        redistribute(banks)
        self.assertEqual([0, 2, 3, 4], banks)

    def test_fourth_cycle(self):
        banks = [0, 2, 3, 4]
        redistribute(banks)
        self.assertEqual([1, 3, 4, 1], banks)

    def test_fifth_cycle(self):
        banks = [1, 3, 4, 1]
        redistribute(banks)
        self.assertEqual([2, 4, 1, 2], banks)

    def test_count_steps(self):
        with open("input.txt") as f:
            input = f.readlines()
        input = [int(item) for sublist in input for item in sublist.strip().split('\t')]
        known_sequences = [list(input)]
        steps = 0
        while True:
            redistribute(input)
            steps += 1
            if input in known_sequences:
                break
            known_sequences.append(list(input))
        print(steps)


if __name__ == '__main__':
    unittest.main()


def redistribute(banks):
    most_occupied = banks.index(max(banks))
    blocks = banks[most_occupied]
    banks[most_occupied] = 0
    index = most_occupied + 1
    for b in range(0, blocks):
        if index >= len(banks):
            index = 0
        banks[index] += 1
        index += 1
