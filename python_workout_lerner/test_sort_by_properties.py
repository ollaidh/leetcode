import unittest


def sort_people_by_first_last_name(people: list[dict]) -> list[dict]:
    people_sorted = sorted(people, key=lambda x: [x['last'], x['first']])
    return people_sorted


def sort_seq_by_abs(seq: list) -> list:
    seq_sorted = sorted(seq, key=lambda x: abs(x))
    return seq_sorted


def sort_by_vowels(seq: list[str]) -> list[str]:
    def count_vowels(word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counter = 0
        for letter in word:
            if letter in vowels:
                counter += 1
        return counter

    seq_sorted = sorted(seq, key=lambda x: count_vowels(x))
    return seq_sorted


def sort_by_sum(seq: list[list]) -> list[list]:
    seq_sorted = sorted(seq, key=lambda x: sum(x))
    return seq_sorted


class TestSorting(unittest.TestCase):
    def test_sort_people_by_first_last_name(self):
        self.assertEqual([
            {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
            {'first': 'Julia', 'last': 'Roberts', 'email': 'actress@hollywood.com'},
            {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'}],
            sort_people_by_first_last_name([
                {'first': 'Julia', 'last': 'Roberts', 'email': 'actress@hollywood.com'},
                {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
                {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'}],
            ))

    def test_sort_seq_by_abs(self):
        self.assertEqual([1, 2, 3, -5, -9, 100], sort_seq_by_abs([-9, 1, 3, 2, -5, 100]))

    def test_sort_by_vowels(self):
        self.assertEqual(['xxx', 'iz', 'abca', 'fooo', 'eeeek'],
                         sort_by_vowels(['abca', 'iz', 'xxx', 'eeeek', 'fooo']))

    def test_sort_by_sum(self):
        self.assertEqual([[], [2], [1, 1, 1, 1], [4, 5]], sort_by_sum([[4, 5], [], [1, 1, 1, 1], [2]]))


if __name__ == '__main__':
    unittest.main()
