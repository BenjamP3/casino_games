# Python Packages
from re import L
from tkinter import *
import sys
from PIL import Image, ImageTk

from Card import Card
from Deck import Deck
from Calculations import *


def printError(best_hand, expectedHand):
    print(f"""Expected: 
    {best_hand[0].prettyPrint()}
    {best_hand[1].prettyPrint()}
    {best_hand[2].prettyPrint()}
    {best_hand[3].prettyPrint()}
    {best_hand[4].prettyPrint()}
Actual:
    {expectedHand[0].prettyPrint()}
    {expectedHand[1].prettyPrint()}
    {expectedHand[2].prettyPrint()}
    {expectedHand[3].prettyPrint()}
    {expectedHand[4].prettyPrint()}""")


def equalHands(hand1, hand2):
    is_equal = 1
    if len(hand1) == len(hand2) and len(hand1) == 5:
        for index in range(len(hand2)):
            if hand1[index].num != hand2[index].num or hand1[index].suit != hand2[index].suit:
                is_equal = 0
    else:
        is_equal = 0

    return is_equal


def testcheckStraightHand1():
    tmp_str = ""
    player1Hand = [Card(7, "Diamonds"), Card(12, "Spades")]
    boardHand = [Card(6, "Clubs"), Card(14, "Clubs"), Card(
        9, "Spades"), Card(8, "Diamonds"), Card(5, "Clubs")]

    best_hand, tmp_str = calculateHand(player1Hand, boardHand)

    expectedHand = [Card(9, "Spades"), Card(8, "Diamonds"), Card(
        7, "Diamonds"), Card(6, "Clubs"), Card(5, "Clubs")]

    return equalHands(best_hand, expectedHand)


def testcheckStraightHand2():
    tmp_str = ""
    result = 0
    player1Hand = [Card(7, "Diamonds"), Card(6, "Spades")]
    boardHand = [Card(6, "Clubs"), Card(14, "Clubs"), Card(
        9, "Spades"), Card(8, "Diamonds"), Card(5, "Clubs")]

    best_hand, tmp_str = calculateHand(player1Hand, boardHand)

    expectedHand = [Card(9, "Spades"), Card(8, "Diamonds"), Card(
        7, "Diamonds"), Card(6, "Clubs"), Card(5, "Clubs")]

    expectedHand2 = [Card(9, "Spades"), Card(8, "Diamonds"), Card(
        7, "Diamonds"), Card(6, "Spades"), Card(5, "Clubs")]

    result = equalHands(best_hand, expectedHand)
    if result == 0:
        result = equalHands(best_hand, expectedHand2)
        if result == 0:
            printError(best_hand, expectedHand)

    return result


def testcheckStraightHand3():
    tmp_str = ""
    player1Hand = [Card(3, "Diamonds"), Card(10, "Spades")]
    boardHand = [Card(2, "Clubs"), Card(14, "Clubs"), Card(
        9, "Spades"), Card(4, "Diamonds"), Card(5, "Clubs")]

    best_hand, tmp_str = calculateHand(player1Hand, boardHand)

    expectedHand = [Card(5, "Clubs"), Card(4, "Diamonds"), Card(
        3, "Diamonds"), Card(2, "Clubs"), Card(14, "Clubs")]

    return equalHands(best_hand, expectedHand)


def testcheckStraightFlush1():
    tmp_str = ""
    player1Hand = [Card(7, "Diamonds"), Card(6, "Diamonds")]
    boardHand = [Card(11, "Clubs"), Card(3, "Hearts"), Card(
        9, "Diamonds"), Card(8, "Diamonds"), Card(5, "Diamonds")]

    best_hand, tmp_str = calculateHand(player1Hand, boardHand)

    expectedHand = [Card(9, "Diamonds"), Card(8, "Diamonds"), Card(
        7, "Diamonds"), Card(6, "Diamonds"), Card(5, "Diamonds")]

    return equalHands(best_hand, expectedHand)


def main():
    tests = [testcheckStraightHand1, testcheckStraightHand2,
             testcheckStraightHand3, testcheckStraightFlush1]
    count_of_tests = len(tests)
    sum_of_working_tests = 0

    for test in tests:
        tmp_result = test()
        sum_of_working_tests += tmp_result
        if tmp_result == 0:
            print("Test Failed - ", test.__name__)

    print(
        f'TESTS - Successful: {sum_of_working_tests}. Total: {count_of_tests}.')


if __name__ == "__main__":
    main()
