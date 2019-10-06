#!/usr/bin/env python3

class Person:
    """
    A class used to represent a Person (player or dealer)

    ...

    Attributes
    ----------
    type : str
        whether player or dealer
    cards : list
        cards held by person
    name : str
        name of Person (default 'Jack')

    Methods
    -------
    get_name()
        Returns the persons name

    is_player()
        Returns True if type of Person is player, false if not

    reveal()
        Peeks top of card stack and returns it

    empty_cards()
        Resets attribute cards to empty list

    get_value()
        Calculates and returns values of attribute cards
    """

    def __init__(self, type, cards, name = "Jack"):
        self.type = type    
        self.cards = cards
        self.name = name


    def get_name(self):
        return self.name


    def is_player(self):
        if self.type == 'player':
            return True
        return False

    
    def reveal(self, hand):
        return self.cards[hand-1]

    
    def empty_cards(self):
        self.cards = []


    def get_value(self):
        value = [0]

        if not self.cards:
            return value
        hasA = False

        for i in self.cards:
            if str(i).isdigit():
                value[0] += i
            else:
                if i == 'A':
                    hasA = True
                else:  # if element is face card, count it as 10
                    value[0] += 10

        if hasA:
            value[0] += 1
            value.append(value[0] + 10)

        return value
