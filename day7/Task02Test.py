import unittest


class Task02Test(unittest.TestCase):

    def test_finding_root(self):
        root_name = 'bpvhwhh'
        with open("input.txt") as f:
            input = f.readlines()
        map = parse_input(input)
        self.sum_child_weights(map, root_name)

    def sum_child_weights(self, tree, name):
        values = tree[name].values()
        if len(values) > 0:
            if len(values[0]) > 0:
                childs = values[0]
                summary_weight = 0
                childs_weights = []
                for child in childs:
                    weight = self.sum_child_weights(tree, child)
                    summary_weight += weight
                    childs_weights.append(weight)
                if not check_eq(childs_weights):
                    self.assertTrue(False, {name: childs_weights})
                return tree[name].keys()[0] + summary_weight
            else:
                return tree[name].keys()[0]
        else:
            return tree[name].keys()[0]


def check_eq(lst):
    return lst[1:] == lst[:-1]


def parse_input(input):
    map = dict()
    for line in input:
        name_and_childs = line.split('->')
        name = name_and_childs[0].split(' ')[0]
        weight = int(name_and_childs[0].split(' ')[1].replace('(', '').replace(')', ''))
        if len(name_and_childs) > 1:
            ref = name_and_childs[1].split(',')
            ref_stripped = [x.strip() for x in ref]
            map[name] = {weight: ref_stripped}
        else:
            map[name] = {weight: []}
    return map


if __name__ == '__main__':
    unittest.main()
