# Python Packages
from re import L
from tkinter import *
import sys
from PIL import Image, ImageTk

from Card import Card


def sortHand(card):
    return card.num


def checkhighCard(totalHand, counts, suits, values):
    hand = []

    sorted_values = list(values)
    sorted_values.sort(reverse=True)
    for val in sorted_values:
        for card in totalHand:
            if card.num == val and len(hand) < 5:
                hand.append(card)

    if len(hand) != 5:
        hand = []

    return hand


def checkPair(totalHand, counts, suits, values):
    hand = []
    nums_used = []
    breakout_flag = False

    # Get first pair
    for count in counts:
        if counts[count] == 2:
            nums_used.append(count)
            breakout_flag = True
            for card in totalHand:
                if card.num == count:
                    hand.append(card)
            if breakout_flag:
                break

    breakout_flag = False

    # Get three other cards
    if len(nums_used) > 0:
        sorted_values = list(values)
        sorted_values.sort(reverse=True)
        for val in sorted_values:
            if val not in nums_used:
                for card in totalHand:
                    if card.num == val and len(hand) < 5:
                        hand.append(card)

    if len(hand) != 5:
        hand = []

    return hand


def check2Pair(totalHand, counts, suits, values):
    hand = []
    nums_used = []
    breakout_flag = False

    # Get first pair
    for count in counts:
        if counts[count] == 2:
            nums_used.append(count)
            breakout_flag = True
            for card in totalHand:
                if card.num == count:
                    hand.append(card)
            if breakout_flag:
                break

    breakout_flag = False

    # Get second pair
    if len(nums_used) > 0:
        for count in counts:
            if count not in nums_used and counts[count] == 2:
                breakout_flag = True
                nums_used.append(count)
                for card in totalHand:
                    if card.num == count:
                        hand.append(card)
                if breakout_flag:
                    break

    # Get 1 remaining card
    if len(nums_used) > 1:
        sorted_values = list(values)
        sorted_values.sort(reverse=True)
        for val in sorted_values:
            if val not in nums_used:
                for card in totalHand:
                    if card.num == val and len(hand) < 5:
                        hand.append(card)

    if len(hand) != 5:
        hand = []

    return hand


def check3Kind(totalHand, counts, suits, values):
    hand = []
    nums_used = []
    breakout_flag = False
    result_string = ""

    for count in counts:
        if counts[count] == 3:
            breakout_flag = False
            nums_used.append(count)
            for card in totalHand:
                if card.num == count:
                    hand.append(card)
            if breakout_flag:
                break

    # Get remaining 2 cards
    if len(nums_used) > 0:
        sorted_values = list(values)
        sorted_values.sort(reverse=True)
        for val in sorted_values:
            if val not in nums_used:
                for card in totalHand:
                    if card.num == val and len(hand) < 5:
                        hand.append(card)
    if len(hand) != 5:
        hand = []

    return hand


def checkStraight(totalHand, counts, suits, values):
    # ADD IN STRAIGHT FROM 5, 4, 3, 2, ACE (val of 14)

    hand = []
    card_hand = []
    breakout_flag = False
    sorted_values = list(values)
    sorted_values.sort(reverse=True)

    if len(sorted_values) >= 5:
        for run in range(0, len(sorted_values) - 3):  # len(list) - 4
            hand = [sorted_values[run]]
            for index in range(1, len(sorted_values)):
                if index + run < len(sorted_values) and (hand[len(hand) - 1] == sorted_values[index + run] + 1):
                    hand.append(sorted_values[index + run])
                if hand[len(hand) - 1] == 2 and sorted_values[0] == 14 and len(hand) == 4:
                    hand.append(sorted_values[0])
                if len(hand) == 5:
                    breakout_flag = True
                if breakout_flag:
                    break
            if breakout_flag:
                break

    if len(hand) != 5:
        hand = []
    else:
        for num in hand:
            breakout_flag = False
            for card in totalHand:
                if card.num == num:
                    card_hand.append(card)
                    breakout_flag = True
                if breakout_flag:
                    break

    return card_hand


def checkFlush(totalHand, counts, suits, values):
    hand = []

    for suit in suits:
        if (suits[suit] >= 5):
            for card in totalHand:
                if card.suit == suit and len(hand) < 5:
                    hand.append(card)

    if len(hand) != 5:
        hand = []

    return hand


def checkFullHouse(totalHand, counts, suits, values):
    hand = []
    nums_used = []
    breakout_flag = False

    for count in counts:
        if counts[count] == 3:
            nums_used.append(count)
            breakout_flag = True
            for card in totalHand:
                if card.num == count:
                    hand.append(card)
            if breakout_flag:
                break

    breakout_flag = False
    for count in counts:
        if counts[count] == 2 and count not in nums_used:
            nums_used.append(count)
            breakout_flag = True
            for card in totalHand:
                if card.num == count:
                    hand.append(card)
            if breakout_flag:
                break

    if len(hand) != 5:
        hand = []

    return hand


def checkQuads(totalHand, counts, suits, values):
    hand = []
    nums_used = []
    breakout_flag = False

    for count in counts:
        if counts[count] == 4:
            nums_used.append(count)
            breakout_flag = True
            for card in totalHand:
                if card.num == nums_used[0]:
                    hand.append(card)
            if breakout_flag:
                break

    # Get 1 remaining card
    if len(nums_used) > 0:
        sorted_values = list(values)
        sorted_values.sort(reverse=True)
        for val in sorted_values:
            if val not in nums_used:
                for card in totalHand:
                    if card.num == val and len(hand) < 5:
                        hand.append(card)

    if len(hand) != 5:
        hand = []

    return hand


def checkStraightFlush(totalHand, counts, suits, values):
    hand = []
    straight_hand = []
    flush_hand = []

    # Cop out way
    straight_hand = checkStraight(totalHand, counts, suits, values)
    flush_hand = checkFlush(totalHand, counts, suits, values)

    if len(straight_hand) == len(flush_hand) and len(straight_hand) == 5:
        for index in range(len(straight_hand)):
            if straight_hand[index].num == flush_hand[index].num and straight_hand[index].num == flush_hand[index].num:
                hand.append(straight_hand[index])

    # Innovative way

    if len(hand) != 5:
        hand = []

    return hand


def checkRoyalFlush(totalHand, counts, suits, values):
    hand = []

    hand = checkStraightFlush(totalHand, counts, suits, values)
    if len(hand) != 5 or hand[0].num != 14:
        hand = []

    return hand


def calculateHand(player1Hand, boardHand):  # Determines the best hand for this player
    totalHand = player1Hand + boardHand
    totalHand.sort(reverse=True, key=sortHand)
    counts = {}
    suits = {}
    values = set()
    best_hand = list()

    for card in totalHand:
        values.add(card.num)
        if card.num in counts:
            counts[card.num] += 1
        else:
            counts[card.num] = 1
        if card.suit in suits:
            suits[card.suit] += 1
        else:
            suits[card.suit] = 1

    best_hand = checkRoyalFlush(totalHand, counts, suits, values)
    if len(best_hand) == 0:
        best_hand = checkStraightFlush(totalHand, counts, suits, values)
        if len(best_hand) == 0:
            best_hand = checkQuads(totalHand, counts, suits, values)
            if len(best_hand) == 0:
                best_hand = checkFullHouse(totalHand, counts, suits, values)
                if len(best_hand) == 0:
                    best_hand = checkFlush(totalHand, counts, suits, values)
                    if len(best_hand) == 0:
                        best_hand = checkStraight(
                            totalHand, counts, suits, values)
                        if len(best_hand) == 0:
                            best_hand = check3Kind(
                                totalHand, counts, suits, values)
                            if len(best_hand) == 0:
                                best_hand = check2Pair(
                                    totalHand, counts, suits, values)
                                if len(best_hand) == 0:
                                    best_hand = checkPair(
                                        totalHand, counts, suits, values)
                                    if len(best_hand) == 0:
                                        best_hand = checkhighCard(
                                            totalHand, counts, suits, values)
                                        result_string = "High Card"
                                    else:
                                        result_string = "Pair"
                                else:
                                    result_string = "2 Pair"
                            else:
                                result_string = "3 of a Kind"
                        else:
                            result_string = "Straight"
                    else:
                        result_string = "Flush"
                else:
                    result_string = "Full House"
            else:
                result_string = "Set of Quads"
        else:
            result_string = "Straight Flush"
    else:
        result_string = "Royal Flush"

    return best_hand, result_string
