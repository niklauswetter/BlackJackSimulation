from enum import Enum
import random


class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


class Value(Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


class Card:
    def __init__(self, suit: Suit, value: Value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'The {self.value.value} of {self.suit.value}'


class Deck:
    def __init__(self, count: int = 1):
        # The count parameter dictates how many full decks will be shuffled
        self.cards = []
        self.drawn = []

        for n in range(0, count):
            for s in Suit:
                for v in Value:
                    self.cards.append(Card(s, v))

    def print_deck(self):
        for c in self.cards:
            print(c)

    def print_drawn(self):
        for c in self.drawn:
            print(c)

    def draw(self):
        c = random.choice(self.cards)
        self.cards.remove(c)
        self.drawn.append(c)
        return c
