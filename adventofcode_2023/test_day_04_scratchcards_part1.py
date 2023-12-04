import pathlib
import unittest

def get_cars_sets(line: str) -> tuple[set[str], list[str]]:
    line = line.split(':')
    cards = line[1].split('|')
    cards[0] = cards[0].lstrip()
    cards[0] = cards[0].rstrip()
    cards[1] = cards[1].lstrip()
    cards[1] = cards[1].rstrip()
    winning = cards[0].split()
    have = cards[1].split()
    return set(winning), have


def scratchcards(input_path: str):
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    total_worth = 0
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            winning_cards, have_cards = get_cars_sets(line)
            curr_worth = 0
            for card in have_cards:
                if card in winning_cards:
                    if curr_worth == 0:
                        curr_worth = 1
                    else:
                        curr_worth *= 2
            total_worth += curr_worth
    return total_worth


class TestScratchcards(unittest.TestCase):
    def test_scratchcards(self):
        self.assertEqual(1, scratchcards('input_day_04_scratchcards.dat'))
