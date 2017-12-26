import unittest


class Task01Test(unittest.TestCase):

    def test_finding_root(self):
        referenced = []
        unreferenced = []
        with open("input.txt") as f:
            input = f.readlines()
        for line in input:
            name_and_childs = line.split('->')
            if len(name_and_childs) > 1:
                ref = name_and_childs[1].split(',')
                ref_stripped = [x.strip() for x in ref]
                referenced.extend(ref_stripped)
            name = name_and_childs[0].split(' ')[0]
            if name not in referenced:
                unreferenced.append(name)
        root = filter(lambda x: x not in referenced, unreferenced)
        print(root)


if __name__ == '__main__':
    unittest.main()
