import unittest
import re


class Task01Test(unittest.TestCase):

    def test_parse_operation_register(self):
        line = "a inc 10 if a > 1"
        self.assertEqual("a", parse(line)['operation_register'])

    def test_parse_operation(self):
        line = "a inc 10 if a > 1"
        self.assertEqual("inc", parse(line)['operation'])

    def test_parse_operation_value(self):
        line = "a inc 10 if a > 1"
        self.assertEqual("10", parse(line)['operation_value'])

    def test_parse_condition_register(self):
        line = "a inc 10 if a > 1"
        self.assertEqual("a", parse(line)['condition_register'])

    def test_parse_condition(self):
        line = "a inc 10 if a > 1"
        self.assertEqual(">", parse(line)['condition'])

    def test_parse_condition_value(self):
        line = "a inc 10 if a > 1"
        self.assertEqual("1", parse(line)['condition_value'])


def parse(line):
    parsed_line = re.search("([a-z]) (inc|dec) (-?\d+) if ([a-z]) (>|<|!=|==|>=|<=) (-?\d+)", line)
    return {
        'operation_register': parsed_line.group(1),
        'operation': parsed_line.group(2),
        'operation_value': parsed_line.group(3),
        'condition_register': parsed_line.group(4),
        'condition': parsed_line.group(5),
        'condition_value': parsed_line.group(6)
    }


if __name__ == '__main__':
    unittest.main()
