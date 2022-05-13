from .deck import Deck


class Player:
    def __init__(self, playerName, playerCurrency, playerNumber):
        self.playerName = playerName
        self.playerHand = Deck(str(self.playerName))
        self.playerCurrency = playerCurrency
        self.PlayerNumber = playerNumber

    def burnCard(self):
        self.playerHand.removeCard()
        print(str(self.playerName) + " burnt a card.")

    def dealCard(self, target):
        tempCard = self.playerHand.removeCard()
        print(str(self.playerName) + " dealt a card to " + str(target) + '.')
        target.playerHand.addCard(tempCard)

    def __repr__(self):
        return self.playerName

    def __str__(self):
        return self.playerName
