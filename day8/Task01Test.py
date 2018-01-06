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

    def test_execute_line(self):
        execution_info = parse("a inc 10 if a < 1")
        registers = dict()
        execute(registers, execution_info)
        self.assertEqual(10, registers['a'])

    def test_evaluate_false_condition(self):
        execution_info = parse("a inc 10 if a > 1")
        registers = dict()
        result = evalute_condition(registers, execution_info)
        self.assertFalse(result)

    def test_evaluate_true_condition(self):
        execution_info = parse("a inc 10 if a < 1")
        registers = dict()
        result = evalute_condition(registers, execution_info)
        self.assertTrue(result)

    def test_evaluate_input(self):
        registers = dict()
        with open("input.txt") as f:
            input = f.readlines()
        for line in input:
            parsed = parse(line)
            result = evalute_condition(registers, parsed)
            if result:
                execute(registers, parsed)
        print(max(registers.values()))


def parse(line):
    parsed_line = re.search("([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (>|<|!=|==|>=|<=) (-?\d+)", line)
    return {
        'operation_register': parsed_line.group(1),
        'operation': parsed_line.group(2),
        'operation_value': parsed_line.group(3),
        'condition_register': parsed_line.group(4),
        'condition': parsed_line.group(5),
        'condition_value': parsed_line.group(6)
    }


def execute(registers, execution_info):
    register = execution_info['operation_register']
    register_value = registers.get(register, 0)
    operation = execution_info['operation']
    if operation == 'inc':
        register_value += int(execution_info['operation_value'])
    else:
        register_value -= int(execution_info['operation_value'])
    registers[register] = register_value
    return registers


def evalute_condition(registers, execution_info):
    condition_register = execution_info['condition_register']
    condition_value = execution_info['condition_value']
    register_value = str(registers.get(condition_register, 0))
    return eval(register_value + execution_info['condition'] + condition_value)


if __name__ == '__main__':
    unittest.main()
