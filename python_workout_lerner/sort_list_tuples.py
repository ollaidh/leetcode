import unittest
import operator


class Films:
    sortings = {'name': 0, 'director': 1, 'length': 2}

    @classmethod
    def sort_films(cls, films, *sorting_parameters: str):
        items = [cls.sortings[param] for param in sorting_parameters]
        films_sorted = [film for film in sorted(films, key=operator.itemgetter(*items))]
        return films_sorted


class TestSort(unittest.TestCase):
    def test_sort_films(self):
        self.assertEqual(
            [('Film1', 'Director9', 5), ('Film4', 'Director2', 1), ('Film4', 'Director5', 2)],
            Films.sort_films([('Film4', 'Director5', 2), ('Film4', 'Director2', 1), ('Film1', 'Director9', 5)],
                             'name', 'director'))
        self.assertEqual(
            [('Film2', 'Director2', 1), ('Film4', 'Director5', 2), ('Film1', 'Director9', 5)],
            Films.sort_films([('Film4', 'Director5', 2), ('Film2', 'Director2', 1), ('Film1', 'Director9', 5)],
                             'director'))
        self.assertEqual(
            [('Film2', 'Director2', 1), ('Film2', 'Director2', 2), ('Film2', 'Director2', 5)],
            Films.sort_films([('Film2', 'Director2', 2), ('Film2', 'Director2', 1), ('Film2', 'Director2', 5)],
                             'name', 'director', 'length'))


if __name__ == '__main__':
    unittest.main()
