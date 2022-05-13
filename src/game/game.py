from random import randint
from src.game.player import Player
from src.game.deck import Deck
from src.game.card import Card

DECK_NAME = "New Deck"
DEALER_NAME = "The Dealer"
TABLE_NAME = "The Table"
DEFAULT_PLAYER_COUNT = 5


# Game Class encapsulates the game for reusability via OOP
class Game:
    def __init__(self, numberOfPlayers=None):
        print('-- Welcome to my Game! --')
        if numberOfPlayers is not None:
            self.playerCount = numberOfPlayers
        else:
            self.playerCount = DEFAULT_PLAYER_COUNT

        self.currentDeck = Deck(DECK_NAME)
        self.dealer = Player(DEALER_NAME, 50000, 0)
        self.table = Player(TABLE_NAME, 0, 0)
        self.players = []

    # Create n number of players for the game
    def createPlayers(self):
        print('-- Creating Players --')
        for count in range(1, self.playerCount + 1):
            newPlayer = Player('Player' + str(count), 100, count)
            self.players.append(newPlayer)
            print(str(newPlayer) + " has joined the game.")
        print('-- Players Created --')
        print()

    def buildDeck(self):
        print('-- Shuffling the Deck --')
        cardList = []

        for card in range(1, 53):
            cardList.append(card)

        for slot in range(0, 52):
            oldValue = cardList[slot]
            newSlot = randint(0, 51)
            swappedValue = cardList[newSlot]
            cardList[newSlot] = oldValue
            cardList[slot] = swappedValue

        for slot in range(0, 52):
            newCard = Card(cardList[slot])
            self.currentDeck.addCard(newCard)
        print('-- Deck Shuffled --')
        print('')

    def playGame(self):
        print('-- Starting NEW GAME --')
        self.dealer.playerHand = self.currentDeck
        self.dealer.playerHand.name = DEALER_NAME

        for x in range(0, 2):
            for player in self.players:
                self.dealer.dealCard(player)

        self.players[0].playerHand.display()

        self.dealer.burnCard()
        for x in range(0, 3):
            self.dealer.dealCard(self.table)
        print('--- FLOP ---')
        self.table.playerHand.display()
        print('--- FLOP ---')
        self.dealer.burnCard()
        self.dealer.dealCard(self.table)
        print('--- TURN ---')
        self.table.playerHand.display()
        print('--- TURN ---')
        self.dealer.burnCard()
        self.dealer.dealCard(self.table)
        print('--- RIVER ---')
        self.table.playerHand.display()
        print('--- RIVER ---')
        for player in self.players:
            player.playerHand.display()
        print('-- GAME OVER --')
        print('')
        print('-- Play Again? --')
