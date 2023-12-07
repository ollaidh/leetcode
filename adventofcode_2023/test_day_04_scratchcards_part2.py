import pathlib
import unittest


def get_cards_sets(line: str) -> tuple[int, set[str], list[str]]:
    line = line.split(':')
    card_number = line[0].split()[-1]
    cards = line[1].split('|')
    cards[0] = cards[0].lstrip()
    cards[0] = cards[0].rstrip()
    cards[1] = cards[1].lstrip()
    cards[1] = cards[1].rstrip()
    winning = cards[0].split()
    have = cards[1].split()
    return int(card_number), set(winning), have


def play_card(card: int, winning: set[str], have: list[str]) -> list[int]:
    winners = 0
    for number in have:
        if number in winning:
            winners += 1
    return [i for i in range(card + 1, card + winners + 1)]


def scratchcards(input_path: str):
    cards = {}
    played = []
    to_play = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            number, winning, have = get_cards_sets(line)
            cards[number] = {'winning': winning, 'have': have}
            to_play.append(number)

    while to_play:
        curr_card = to_play.pop()
        played.append(curr_card)
        new_cards = play_card(curr_card, cards[curr_card]['winning'], cards[curr_card]['have'])
        to_play.extend(new_cards)

    return len(played)


class TestScratchcards(unittest.TestCase):
    def test_play_card(self):
        self.assertEqual(
            [2, 3, 4, 5],
            play_card(1, {'41', '48', '83', '86', '17'}, ['83', '86', '6', '31', '17', '9', '48', '53'])
        )
        self.assertEqual(
            [3, 4],
            play_card(2, {'13', '32', '20', '16', '61'}, ['61', '30', '68', '82', '17', '32', '24', '19'])
        )


if __name__ == '__main__':
    result = scratchcards('input_day_04_scratchcards.dat')
    print(result)
