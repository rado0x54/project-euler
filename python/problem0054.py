#!/usr/bin/env python3
"""Project Euler - Problem 54 Module"""

import os
import operator
from collections import Counter

# def map_card_value(str_value):
#     return CARD_VALUE_MAP[str_value]


def build_rank(cards):
    """Returns a card"""

    suits = [c[1] for c in cards]
    flush = suits.count(suits[0]) == len(suits)

    # Build And Sort card values by CARD_VALUE_MAP
    card_vals_desc = sorted([CARD_VALUE_MAP[c[0]]
                             for c in cards], reverse=True)

    straight = all(card_vals_desc[i] - 1 == card_vals_desc[i + 1]
                   for i in range(len(card_vals_desc) - 1))
    royal = straight and (card_vals_desc[0] == CARD_VALUE_MAP['A'])

    # Count occurrences and order by them.
    counter = Counter(card_vals_desc)
    card_counter_sorted = sorted(
        counter.most_common(), key=operator.itemgetter(1, 0), reverse=True)

    # Priority Array:
    card_priority = [c[0] for c in card_counter_sorted]

    # Royal Flush
    if royal and flush:
        return "RF", []  # No Tie-Braker needed

    # Straigt Flush
    if straight and flush:
        return "SF", card_priority

    # Four of a kind
    if card_counter_sorted[0][1] == 4:
        return "FK", card_priority

    # Full House
    if card_counter_sorted[0][1] == 3 and card_counter_sorted[1][1] == 2:
        return "FH", card_priority

    # Flush
    if flush:
        return "FL", card_priority

    # Straight
    if straight:
        return "ST", card_priority

    # Three of a Kind
    if card_counter_sorted[0][1] == 3:
        return "TK", card_priority

    # Two Pair
    if card_counter_sorted[0][1] == 2 and card_counter_sorted[1][1] == 2:
        return "TP", card_priority

    # One Pair
    if card_counter_sorted[0][1] == 2:
        return "OP", card_priority

    # High Card
    return "HC", card_priority


def determine_winner(p1_cards, p2_cards):
    # -1 p1 wins
    # +1 p2 wins
    p1_rank, p1_prio_list = build_rank(p1_cards)
    p2_rank, p2_prio_list = build_rank(p2_cards)
    # print("P1 Cards: {} Rank: {}, Prio: {}".format(p1_cards, p1_rank, p1_prio_list))
    # print("P2 Cards: {} Rank: {}, Prio: {}".format(p2_cards, p2_rank, p2_prio_list))

    if RANK_VALUE_MAP[p1_rank] > RANK_VALUE_MAP[p2_rank]:
        return -1
    elif RANK_VALUE_MAP[p1_rank] < RANK_VALUE_MAP[p2_rank]:
        return 1

    # Evaluate Priority List (has same length for same rank)
    for i in range(0, len(p1_prio_list)):
        if p1_prio_list[i] > p2_prio_list[i]:
            return -1
        elif p1_prio_list[i] < p2_prio_list[i]:
            return 1

    # Draw # Should never happen
    print("Draw of P1 Cards: {} and P2 Cards: {}".format(p1_cards, p2_cards))
    return 0

CARD_SPLIT_VAL = 5


def problem54(fileloc):
    """Problem 54 - Poker hands"""

    p1_wins = 0
    # Read File
    with open(fileloc, 'r') as f:
        for line in f:
            all_cards = line.split()
            p1_cards = all_cards[:CARD_SPLIT_VAL]
            p2_cards = all_cards[CARD_SPLIT_VAL:]
            if determine_winner(p1_cards, p2_cards) < 0:
                p1_wins += 1

    return p1_wins

RANK_VALUE_MAP = {
    "HC": 0,
    "OP": 1,
    "TP": 2,
    "TK": 3,
    "ST": 4,
    "FL": 5,
    "FH": 6,
    "FK": 7,
    "SF": 8,
    "RF": 9
}

CARD_VALUE_MAP = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

FILENAME = 'problem0054.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run():
    """Default Run Method"""
    return problem54(os.path.join(__location__, FILENAME))

if __name__ == '__main__':
    print("Result: ", run())
