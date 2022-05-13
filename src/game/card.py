import math


class Card:
    def __init__(self, value):
        self.valueCode = 0
        self.valueName = ''
        self.suit = ''
        self.name = ''
        self.shortName = ''
        self.shortValue = ''
        suitCode = math.floor(value / 13)
        if suitCode == 1:
            self.suit = 'Hearts'
        elif suitCode == 2:
            self.suit = 'Diamonds'
        elif suitCode == 3:
            self.suit = 'Clubs'
        else:
            self.suit = 'Spades'

        self.valueCode = value % 13 + 1
        if self.valueCode == 1:
            self.valueName = 'Ace'
            self.shortValue = 'A'
        elif self.valueCode == 11:
            self.valueName = 'Jack'
            self.shortValue = 'J'
        elif self.valueCode == 12:
            self.valueName = 'Queen'
            self.shortValue = 'Q'
        elif self.valueCode == 13:
            self.valueName = 'King'
            self.shortValue = 'K'
        else:
            self.valueName = str(self.valueCode)
            self.shortValue = self.valueCode

        self.name = str(self.valueName) + " of " + str(self.suit)
        self.shortName = str(self.shortValue) + '-' + str(self.suit[0])
