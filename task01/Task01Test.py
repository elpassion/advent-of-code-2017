import unittest


def sumOfMatchingFollowers(input):
    matched = []
    for ndx, member in enumerate(input):
        if ndx < len(input) - 1 and input[ndx] == input[ndx + 1]:
            matched.append(int(member))
        if ndx == len(input) - 1 and input[ndx] == input[0]:
            matched.append(int(member))
    return sum(matched)


class Task01Test(unittest.TestCase):
    def test_sample_case(self):
        self.input = "1122"
        self.assertEqual(3, sumOfMatchingFollowers(self.input))

    def test_algorithm_circularity(self):
        self.input = "1111"
        self.assertEqual(4, sumOfMatchingFollowers(self.input))

    def test_zero_matches(self):
        self.input = "1234"
        self.assertEqual(0, sumOfMatchingFollowers(self.input))

if __name__ == '__main__':
    unittest.main()
