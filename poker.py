import random, collections
from itertools import combinations
from operator import attrgetter


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return str(self.rank) + self.suit


class Hand:
    # Initializes and ranks hands.
    def __init__(self, cards):
        self.hand = cards
        self.sorted_hand = []
        self.rank = {}
        self.rank_number = 0
        self.flush = False
        self.straight = False
        quads = [4, 1]
        full_house = [3, 2]
        three_of_a_kind = [3, 1, 1]
        two_pair = [2, 2, 1]
        pair = [2, 1, 1, 1]

        rank_attr = attrgetter("rank")
        suit_attr = attrgetter("suit")
        d = list(self.hand)
        self.sorted_hand = sorted((rank_attr(r) for r in d))
        print(d)
        print(self.sorted_hand)
        p = sorted(collections.Counter(rank_attr(r) for r in d).values(), reverse=True)
        print(p)

        if p == quads:
            self.rank = "Quads"
            self.rank_number = 8
        elif p == full_house:
            self.rank = "Full House"
            self.rank_number = 7
        elif p == three_of_a_kind:
            self.rank = "Three of a Kind"
            self.rank_number = 4
        elif p == two_pair:
            self.rank = "Two Pair"
            self.rank_number = 3
        elif p == pair:
            self.rank = "Pair"
            self.rank_number = 2
        else:
            f = sorted(collections.Counter(suit_attr(r) for r in d).values())
            if f == [5]:
                self.flush = True
            s = sorted(list(self.hand), key=attrgetter("rank"))
            if s[4].rank - s[0].rank == 4 or s[4].rank == 14 and s[3].rank == 5:
                self.straight = True
            if self.flush and self.straight:
                if s[4].rank == 14:
                    self.rank = "Royal Flush"
                    self.rank_number = 10
                else:
                    self.rank = "Straight Flush"
                    self.rank_number = 9
            elif self.flush:
                self.rank = "Flush"
                self.rank_number = 6
            elif self.straight:
                self.rank = "Straight"
                self.rank_number = 5
            else:
                self.rank = "High Card"
                self.rank_number = 1
        print(self.rank)

    def __str__(self):
        return str(self.hand)


class Deck:

    def __init__(self, *cards):
        self.contents = []

    def new_deck(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ["s", "c", "d", "h"]

        for s in suits:
            for r in ranks:
                c = Card(r, s)
                self.contents.append(c)

    def test_deck(self, *r):
        for rr, ss in r:
            c = Card(rr, ss)
            print(c)
            self.contents.append(c)

    def shuffle(self):
        random.shuffle(self.contents)

    def __repr__(self):
        return str(self.contents)


def compare_two_hands(hand1, hand2):
    if hand1.rank_number > hand2.rank_number:
        return hand1
    elif hand1.rank_number < hand2.rank_number:
        return hand2
    else:
        if hand1.rank == "straight":
            if hand1[0] == 14 or hand2[0] == 14:
                return hand1


def compare_hands(*hands_to_be_compared):
    hand_ranks = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Quads", "Straight Flush", "Royal Flush"]
    result = []
    for current_hand in hands_to_be_compared:
        if not result:
            result.append(current_hand)
        else:
            for hand_already_in_list in result:
                if current_hand.rank_number > hand_already_in_list.rank_number:
                    result.insert(hand_already_in_list, current_hand)
                    break
                elif current_hand.rank_number < hand_already_in_list.rank_number:
                    if current_hand in result:
                        result.pop(current_hand)
                        result.insert(hand_already_in_list + 1, current_hand)
                    result.insert(hand_already_in_list + 1, current_hand)
                else:
                    if current_hand.rank == "straight":
                        if current_hand[0] == 14 and hand_already_in_list[0] != 14:
                            result.insert(current_hand, hand_already_in_list + 1)

    return result


#deck = Deck()
#deck.new_deck()
#print(deck.contents)

#a = combinations(deck.contents, 5)
#for xx in list(a):
 #   Hand(xx)


