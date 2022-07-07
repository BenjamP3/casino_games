# Python Packages
from PIL import Image, ImageTk

# Cards were found here:
# - https://boardgames.stackexchange.com/questions/51426/where-can-i-download-high-quality-images-of-poker-cards
# - https://code.google.com/archive/p/vector-playing-cards/downloads

IMG_PATH = '../images/'

face_cards = {
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Ace"
}


class Card:  # Represents 1 card in a deck
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def getName(self):
        return f'{self.num}_of_{self.suit}'

    def getImg(self):
        return f'{IMG_PATH}{self.num}_of_{self.suit}.png'

    def resizedCard(self):
        card_img = Image.open(self.getImg())
        card_pic = ImageTk.PhotoImage(card_img.resize((150, 218)))
        return card_pic

    def prettyPrint(self):
        name = self.num
        if name in face_cards:
            name = face_cards[name]
        return f'{name} of {self.suit}'
