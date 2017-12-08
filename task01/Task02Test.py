import unittest


def sumOfMatchingHalfwayAround(input):
    matched = []
    half_size = int(len(input) / 2)
    for ndx, member in enumerate(input):
        if input[ndx] == input[(ndx + half_size) % len(input)]:
            matched.append(int(member))
    return sum(matched)


class Task01Test(unittest.TestCase):
    def test_sample_case(self):
        self.input = "1212"
        self.assertEqual(6, sumOfMatchingHalfwayAround(self.input))

    def test_zero_matches(self):
        self.input = "1221"
        self.assertEqual(0, sumOfMatchingHalfwayAround(self.input))

    def test_single_match_beginning_with_end(self):
        self.input = "123425"
        self.assertEqual(4, sumOfMatchingHalfwayAround(self.input))

    def test_multiple_matches(self):
        self.input = "123123"
        self.assertEqual(12, sumOfMatchingHalfwayAround(self.input))


if __name__ == '__main__':
    unittest.main()
