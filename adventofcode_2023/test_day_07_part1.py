import unittest
import pathlib


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = [card for card in cards]
        self.bid = bid

    def hand_type(self) -> int:
        counter = {}
        for card in self.cards:
            if card not in counter:
                counter[card] = 0
            counter[card] += 1
        counter = [value for _, value in counter.items()]

        if len(counter) == 1:
            return 7
        elif len(counter) == 2:
            if max(counter) == 4:
                return 6
            return 5
        elif len(counter) == 3:
            if max(counter) == 3:
                return 4
            return 3
        elif len(counter) == 4:
            return 2
        return 1

    def __lt__(self, other) -> bool:
        cards_strength = {
            'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
            '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1
        }
        if self.hand_type() < other.hand_type():
            return True
        elif self.hand_type() > other.hand_type():
            return False
        for card_s, card_o in zip(self.cards, other.cards):
            if cards_strength[card_s] > cards_strength[card_o]:
                return False
            elif cards_strength[card_s] < cards_strength[card_o]:
                return True
        return False

    def __repr__(self):
        return f'Hand({self.cards}, {self.bid})'


def parse_input(input_path: str) -> list[Hand]:
    hands = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            line = line.rstrip().lstrip().split()
            curr_hand = Hand(line[0], int(line[1]))
            hands.append(curr_hand)
    return hands


def total_winnings(hands: list[Hand]) -> int:
    total = 0
    hands = sorted(hands)
    # print(len(hands))
    for i in range(len(hands) - 1, -1, -1):
        total += hands[i].bid * (i + 1)

    return total


def play(input_path: str) -> int:
    hands = parse_input(input_path)
    return total_winnings(hands)


class TestHands(unittest.TestCase):
    def test_hand_type(self):
        hand1 = Hand('AAAAA', 111)
        self.assertEqual(7, hand1.hand_type())
        hand2 = Hand('AA8AA', 111)
        self.assertEqual(6, hand2.hand_type())
        hand3 = Hand('23332', 111)
        self.assertEqual(5, hand3.hand_type())
        hand4 = Hand('TTT98', 111)
        self.assertEqual(4, hand4.hand_type())
        hand5 = Hand('23432', 111)
        self.assertEqual(3, hand5.hand_type())
        hand6 = Hand('A23A4', 111)
        self.assertEqual(2, hand6.hand_type())
        hand7 = Hand('23456', 111)
        self.assertEqual(1, hand7.hand_type())

    def test_ln_hands(self):
        hand1 = Hand('AAAAA', 111)
        hand2 = Hand('JJJJJ', 111)
        self.assertTrue(hand1 > hand2)

        hand1 = Hand('JJJJJ', 111)
        hand2 = Hand('JJ8JJ', 111)
        self.assertTrue(hand1 > hand2)

        hand1 = Hand('AAQQQ', 111)
        hand2 = Hand('QQ8QQ', 111)
        self.assertTrue(hand1 < hand2)

        hand1 = Hand('12345', 111)
        hand2 = Hand('11223', 111)
        self.assertTrue(hand1 < hand2)

        hand1 = Hand('T55J5', 111)
        hand2 = Hand('QQQJA', 111)
        self.assertTrue(hand1 < hand2)

        hand1 = Hand('KTJJT', 111)
        hand2 = Hand('KK677', 111)
        self.assertTrue(hand1 < hand2)

    def test_total_winnings(self):
        hands = [
            Hand('32T3K', 765),
            Hand('T55J5', 684),
            Hand('KK677', 28),
            Hand('KTJJT', 220),
            Hand('QQQJA', 483)
        ]
        self.assertEqual(6440, total_winnings(hands))


if __name__ == '__main__':
    result = play('input_day_07_part1.dat')
    print(result)
