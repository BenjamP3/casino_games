# Python Packages
from asyncio.windows_events import NULL
import random

# Imported Files
from Card import Card


class Deck:  # Represents a deck of 52 cards from 2 to ace
    def __init__(self):
        self.deck = []
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
        for suit in suits:
            for num in range(2, 15):
                self.deck.append(Card(num, suit))

    def printDeck(self):
        for card in self.deck:
            print(card.getName())

    def getCard(self):
        if len(self.deck) > 0:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card
        else:
            print("No cards left.")
            return NULL
