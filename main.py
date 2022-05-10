from random import randint
import math

class Card:
    def __init__(self, value):
        self.valueCode = 0
        self.valueName = ''
        self.suit = ''
        self.name = ''
        self.shortName = ''
        self.shortValue = ''
        suitCode = math.floor(value/13)
        if suitCode == 1:
            self.suit = 'Hearts'
        elif suitCode == 2:
            self.suit = 'Diamonds'
        elif suitCode == 3:
            self.suit = 'Clubs'
        else:
            self.suit = 'Spades'

        self.valueCode = value%13+1
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

def DeckBuilder():
    cardList = []

    for card in range (1, 53):
        cardList.append(card)

    #print(str(cardList))


    for slot in range (0, 52):
        oldValue = cardList[slot]
        newSlot = randint(0, 51)
        swappedValue = cardList[newSlot]
        cardList[newSlot] = oldValue
        cardList[slot] = swappedValue

    #print(str(cardList))

    #shuffleChecker = {}
    #for x in range(1, 53):
    #    shuffleChecker[x] = 0

    #for card in cardList:
    #    shuffleChecker[card] = shuffleChecker[card] + 1

    #print(str(shuffleChecker))

    for slot in range(0, 52):
        newCard = Card(cardList[slot])
        currentDeck.addCard(newCard)

playerCount = 5
dealer = Player("The Dealer", 50000, 0)
currentDeck = Deck("New Deck")
table = Player('The Table', 0, 0)
players = []
for count in range(1, playerCount+1):
    newPlayer = Player('Player' + str(count), 100, count)
    players.append(newPlayer)
    print(str(newPlayer) + " has joined the game.")
#print(str(players))

DeckBuilder()
dealer.playerHand = currentDeck
dealer.playerHand.name = 'The Dealer'

#hand = Deck("Hand")

for x in range(0, 2):
    for player in players:
        dealer.dealCard(player)

players[0].playerHand.display()

dealer.burnCard()
for x in range(0, 3):
    dealer.dealCard(table)
print('                 ---FLOP---')
table.playerHand.display()
print('                 ---FLOP---')
dealer.burnCard()
dealer.dealCard(table)
print('                    ---TURN---')
table.playerHand.display()
print('                    ---TURN---')
dealer.burnCard()
dealer.dealCard(table)
print('                       ---RIVER---')
table.playerHand.display()
print('                       ---RIVER---')
for player in players:
    player.playerHand.display()

print("NEW GAME")
DeckBuilder()

