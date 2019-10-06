#!/usr/bin/env python3

import random


class Deck:
    """
        class used to represent a Deck of Cards

        ...

        Attributes
        ----------
        cards : list
            deck of cards

        Methods
        -------
        new_deck()
            Re-initializes list of cards

        shuffle()
            Randomises order of cards

        deal()
            Returns top card in deck
    """

    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'K', 'Q'] * 4

    
    def new_deck(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'K', 'Q'] * 4


    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self):
        return self.cards.pop()
    