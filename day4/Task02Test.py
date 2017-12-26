import unittest
import itertools


class Task02Test(unittest.TestCase):

    def test_count_valid_passphrases(self):
        with open("input.txt") as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        count = len(filter(lambda x: is_valid(x), content))
        print(count)

    def test_simple_valid_passphrase(self):
        self.assertTrue(is_valid("ab"))

    def test_passphrase_with_duplicates_is_invalid(self):
        self.assertFalse(is_valid("aa aa"))

    def test_passphrase_with_anagram_is_invalid(self):
        self.assertFalse(is_valid("ab ba"))


if __name__ == '__main__':
    unittest.main()


def is_valid(passphrase):
    return has_no_duplicates(passphrase) and has_no_anagrams(passphrase)


def has_no_duplicates(passphrase):
    chunks = passphrase.split()
    return len(set(chunks)) == len(chunks)


def has_no_anagrams(passphrase):
    chunks = passphrase.split()
    for chunk in chunks:
        chars = list(chunk)
        permutations = set(itertools.permutations(chars))
        generated_anagrams = [''.join(x) for x in permutations]
        generated_anagrams.remove(chunk)
        if any(anagram in chunks for anagram in generated_anagrams):
            return False

    return True
