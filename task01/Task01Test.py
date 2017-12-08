import unittest


def sumOfMatchingFollowers(input):
    matched = []
    for ndx, member in enumerate(input):
        if ndx < len(input) - 1 and input[ndx] == input[ndx + 1]:
            matched.append(int(member))
    return sum(matched)


class Task01Test(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_first_example(self):
        self.input = "1122"
        self.assertEqual(3, sumOfMatchingFollowers(self.input))


if __name__ == '__main__':
    unittest.main()
