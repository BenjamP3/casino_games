# Python Packages
from re import L
from tkinter import *
import sys
from PIL import Image, ImageTk

# Imported Files
from Card import Card, IMG_PATH
from Deck import Deck
from Calculations import *

HIGHLIGHT_COLOR = "yellow"
PLAYING_AREA_COLOR = "#803300"
BG_BORDER = 6

global boardHand, player1Hand


def highlightCards(best_hand, boardHand, player1Hand, flop1_label, flop2_label, flop3_label,
                   turn_label, river_label, p1c1_label, p1c2_label):  # Highlights the corresponding cards in the best hand onto the table
    for card in best_hand:
        if card in player1Hand:
            for index in range(len(player1Hand)):
                if card.num == player1Hand[index].num and card.suit == player1Hand[index].suit:
                    if index == 0:
                        p1c1_label.config(bg=HIGHLIGHT_COLOR)
                    elif index == 1:
                        p1c2_label.config(bg=HIGHLIGHT_COLOR)
                    else:
                        print("Error highlighting the cards in playersHand")
        elif card in boardHand:
            for index in range(len(boardHand)):
                if card.num == boardHand[index].num and card.suit == boardHand[index].suit:
                    if index == 0:
                        flop1_label.config(bg=HIGHLIGHT_COLOR)
                    elif index == 1:
                        flop2_label.config(bg=HIGHLIGHT_COLOR)
                    elif index == 2:
                        flop3_label.config(bg=HIGHLIGHT_COLOR)
                    elif index == 3:
                        turn_label.config(bg=HIGHLIGHT_COLOR)
                    elif index == 4:
                        river_label.config(bg=HIGHLIGHT_COLOR)
                    else:
                        print("Error highlighting the cards in boardHand")


def dealPlayer(deck, player1Hand, p1c1_label, p1c2_label):  # Obtain cards for this player
    player1_card1 = deck.getCard()
    player1Hand.append(player1_card1)
    img = player1_card1.resizedCard()
    p1c1_label.image = img
    p1c1_label.config(image=img, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)

    player1_card2 = deck.getCard()
    player1Hand.append(player1_card2)
    img = player1_card2.resizedCard()
    p1c2_label.image = img
    p1c2_label.config(image=img, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)


def dealFlop(deck, boardHand, player1Hand, flop1_label, flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button):  # Obtains cards for the flop
    flop1 = deck.getCard()
    boardHand.append(flop1)
    img = flop1.resizedCard()
    flop1_label.image = img
    flop1_label.config(image=img)

    flop2 = deck.getCard()
    boardHand.append(flop2)
    img = flop2.resizedCard()
    flop2_label.image = img
    flop2_label.config(image=img)

    flop3 = deck.getCard()
    boardHand.append(flop3)
    img = flop3.resizedCard()
    flop3_label.image = img
    flop3_label.config(image=img)

    play_button.config(text="Deal Turn", command=lambda: dealTurn(deck, boardHand, player1Hand, flop1_label,
                       flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button))


def dealTurn(deck, boardHand, player1Hand, flop1_label, flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button):  # Obtains cards for the turn
    turn = deck.getCard()
    boardHand.append(turn)
    img = turn.resizedCard()
    turn_label.image = img
    turn_label.config(image=img)

    play_button.config(text="Deal River", command=lambda: dealRiver(deck, boardHand, player1Hand, flop1_label,
                       flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button))


def dealRiver(deck, boardHand, player1Hand, flop1_label, flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button):  # Obtains cards for the river
    result_string = ""

    # Set river card on board
    river = deck.getCard()
    boardHand.append(river)
    img = river.resizedCard()
    river_label.image = img
    river_label.config(image=img)

    # Reset play button
    play_button.config(text="Play Again", command=lambda: startDealing(
        flop1_label, flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button))

    # Retrieve the best hand
    best_hand, result_string = calculateHand(player1Hand, boardHand)
    hand_score.config(
        text=f'SCORE: {result_string}\nBEST HAND: {best_hand[0].prettyPrint()}, {best_hand[1].prettyPrint()}, {best_hand[2].prettyPrint()}, {best_hand[3].prettyPrint()}, {best_hand[4].prettyPrint()}')

    # Highlight the best hand on the board
    highlightCards(best_hand, boardHand, player1Hand, flop1_label, flop2_label, flop3_label,
                   turn_label, river_label, p1c1_label, p1c2_label)


def startDealing(flop1_label, flop2_label, flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button):  # Create the GUI body
    # Create starting deck
    deck = Deck()
    boardHand = []
    player1Hand = []

    # Retrieve player cards
    dealPlayer(deck, player1Hand, p1c1_label, p1c2_label)
    play_button.config(text="Deal Flop", command=lambda: dealFlop(deck, boardHand, player1Hand, flop1_label, flop2_label,
                       flop3_label, turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button))

    hand_score.config(text="SCORE:\nBEST HAND:")

    # Fill in board with joker cards before reveal
    card_img = Image.open(f'{IMG_PATH}red_joker.png')
    card_pic = ImageTk.PhotoImage(card_img.resize((150, 218)))

    flop1_label.image = card_pic
    flop1_label.config(image=card_pic, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)
    flop2_label.image = card_pic
    flop2_label.config(image=card_pic, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)
    flop3_label.image = card_pic
    flop3_label.config(image=card_pic, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)
    turn_label.image = card_pic
    turn_label.config(image=card_pic, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)
    river_label.image = card_pic
    river_label.config(image=card_pic, bg=PLAYING_AREA_COLOR, bd=BG_BORDER)


def main():  # Main Func
    # Initial setup
    # - Create root frame for GUI
    root = Tk()
    root.title("TEXAS HOLD 'EM POKER")
    # root.geometry("1200x900")
    root.configure(background="green")

    # - Create initial inner frame
    my_frame = Frame(root, bg="green")
    my_frame.pack(pady=20)

    # Create base GUI
    # - Create Board row (frame) for 5 public cards
    board_grame = LabelFrame(my_frame, text="Board",
                             bd=0, bg=PLAYING_AREA_COLOR)
    board_grame.grid(row=0, column=0, padx=20)

    # - Create a label for each public card
    flop1_label = Label(board_grame, text="")
    flop1_label.pack(side=LEFT, padx=20, pady=20)

    flop2_label = Label(board_grame, text="")
    flop2_label.pack(side=LEFT, padx=20, pady=20)

    flop3_label = Label(board_grame, text="")
    flop3_label.pack(side=LEFT, padx=20, pady=20)

    turn_label = Label(board_grame, text="")
    turn_label.pack(side=LEFT, padx=20, pady=20)

    river_label = Label(board_grame, text="")
    river_label.pack(side=LEFT, padx=20, pady=20)

    # - Create Player row (frame) for player's 2 private cards
    p1_frame = LabelFrame(my_frame, text="Player", bd=0, bg=PLAYING_AREA_COLOR)
    p1_frame.grid(row=1, column=0, padx=20, pady=20)

    # - Create a label for each player card
    p1c1_label = Label(p1_frame, text="")
    p1c1_label.pack(side=LEFT, padx=20, pady=20)

    p1c2_label = Label(p1_frame, text="")
    p1c2_label.pack(side=LEFT, padx=20, pady=20)

    # - Create score display (frame) to output hand result
    game_result = LabelFrame(my_frame, bd=0, bg="green")
    game_result.grid(row=2, column=0, padx=20)

    hand_score = Label(game_result, text="", bg="lightgrey")
    hand_score.pack(side=LEFT, padx=20, pady=20)

    # - Create input row (frame) for the user's input
    user_input = LabelFrame(my_frame, bd=0, bg="green")
    user_input.grid(row=3, column=0, padx=20)

    play_button = Button(user_input, font="Helvetica")
    play_button.pack(side=LEFT, padx=20)

    cancel_button = Button(user_input, text="Quit Game",
                           font="Helvetica", command=lambda: sys.exit())
    cancel_button.pack(side=LEFT, padx=20)

    # Deal out cards
    startDealing(flop1_label, flop2_label, flop3_label,
                 turn_label, river_label, p1c1_label, p1c2_label, hand_score, play_button)

    # Displays image/game
    root.mainloop()


if __name__ == "__main__":
    main()
