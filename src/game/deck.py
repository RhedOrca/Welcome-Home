from .card import Card


class Deck:
    def __init__(self, name):
        self.name = name
        self.cardSet = []

    def addCard(self, Card):
        self.cardSet.append(Card)

    def removeCard(self):
        removedCard = self.cardSet.pop()
        return removedCard

    def display(self):
        output = []
        for card in self.cardSet:
            output.append(card.shortName)
        print(self.name + ": " + str(output))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
