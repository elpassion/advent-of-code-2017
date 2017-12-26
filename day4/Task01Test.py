import unittest


class Task01Test(unittest.TestCase):

    def test_count_valid_passphrases(self):
        with open("input.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        count = len(filter(lambda x: is_valid(x), content))
        print(count)

    def test_simple_valid_passphrase(self):
        self.assertTrue(is_valid("aa"))

    def test_passphrase_with_duplicates_is_invalid(self):
        self.assertFalse(is_valid("aa aa"))


if __name__ == '__main__':
    unittest.main()


def is_valid(passphrase):
    chunks = passphrase.split()
    return len(set(chunks)) == len(chunks)
