# -*- coding: utf-8 -*-

# Zadanie 1.2 - Fold, Check, Call, Raise...

# Meno: 
# Spolupráca: 
# Použité zdroje: 
# Čas: 6hodin

from copy import deepcopy
from itertools import combinations
# hearts, clubs, spades, diamonds
SUITS = ['H', 'C', 'S', 'D']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
DECK = [(s, v) for s in SUITS for v in VALUES]


def generate_setup():
    # helper function for generating test cases
    from random import sample
    deck = deepcopy(DECK)
    player1_hand = sample(deck, 2)
    for card in player1_hand:
        deck.remove(card)
    player2_hand = sample(deck, 2)
    for card in player2_hand:
        deck.remove(card)
    flop = sample(deck, 3)
    for card in flop:
        deck.remove(card)
    turn = sample(deck, 1)
    for card in turn:
        deck.remove(card)

    return player1_hand, player2_hand, flop, turn


def is_royal_flush(hand):
    
    suit = hand[0][0]
    
    is_same_color = all(s == suit for s,_ in hand)
    is_royal = all(v in VALUES[8:] for _, v in hand)
    
    if is_same_color and is_royal:
        return (True, (14,))
    else:
        return (False, tuple())


def is_straight_flush(hand):
    suit = hand[0][0]
    is_same_color = all(s == suit for s,_ in hand)
    values = sorted([v for _, v in hand])
    is_straight = all(v+1 == values[idx+1] for idx,v in enumerate(values[:-1]))
    if is_same_color and is_straight:
        return True, (max(values),)
    return False, None


def is_four_of_a_kind(hand):
    values = sorted([v for _, v in hand])

    last_4 = list(set(values[1:]))
    first_4 = list(set(values[:-1]))

    if len(last_4) == 1:
        return True, (last_4[0],)
    if len(first_4) == 1:
        return True, (first_4[0],)

    return False, None


def is_full_house(hand):
    values = [v for _, v in hand]
    
    s_values = list(set(values))
    if len(s_values) == 2:
        if (values.count(s_values[0]) == 3 and values.count(s_values[1]) == 2):
            return True, (s_values[0], s_values[1])

        if (values.count(s_values[0]) == 2 and values.count(s_values[1]) == 3):
            return True, (s_values[1], s_values[0])

    return False, None


def is_flush(hand):
    values = [v for _, v in hand]
    if all(s == hand[0][0] for s,_ in hand):
        return True, (max(values),)
    return False, None


def is_straight(hand):
    values = sorted([v for _, v in hand])
    is_straight = all(v+1 == values[idx+1] for idx,v in enumerate(values[:-1]))
    if is_straight:
        return True, (max(values),)
    return False, None


def is_three_of_a_kind(hand):
    values = sorted([v for _, v in hand])
    
    v_count = {v : values.count(v) for v in set(values)}

    for v, vc in v_count.items():
        if vc == 3:
            return True, (v,)

    return False, None


def is_two_pairs(hand):
    values = [v for _, v in hand]
    v_count = {v : values.count(v) for v in set(values)}
    
    v_count_values = sorted(v_count.values())

    if v_count_values == [1, 2, 2]:
        res = [v for v, vc in v_count.items() if vc == 2]
        res_tuple = tuple(sorted(res, reverse=True))
        return True, res_tuple

    return False, None


def is_pair(hand):
    values = sorted([v for _, v in hand])
    v_count = {v : values.count(v) for v in set(values)}
    v_count_values = list(v_count.values())

    if v_count_values.count(2) == 1:
        return True, tuple(v for v, vc in v_count.items() if vc == 2)

    return False, None


def evaluate_hand(hand):
    res = is_royal_flush(hand)
    if res[0]:
        return 9, res[1]

    res = is_straight_flush(hand)
    if res[0]:
        return 8, res[1]

    res = is_four_of_a_kind(hand)
    if res[0]:
        return 7, res[1]

    res = is_full_house(hand)
    if res[0]:
        return 6, res[1]

    res = is_flush(hand)
    if res[0]:
        return 5, res[1]

    res = is_straight(hand)
    if res[0]:
        return 4, res[1]

    res = is_three_of_a_kind(hand)
    if res[0]:
        return 3, res[1]

    res = is_two_pairs(hand)
    if res[0]:
        return 2, res[1]

    res = is_pair(hand)
    if res[0]:
        return 1, res[1]

    return 0, None


def compare_highest_card(hand_1, hand_2):
    values1 = list([v for _, v in hand_1])
    values2 = list([v for _, v in hand_2])
    
    
    for _ in range(5):
        m1 = max(values1)
        m2 = max(values2)
        if m1 > m2:
            return hand_1
        
        if m1 < m2:
            return hand_2
        values1.remove(m1)
        values2.remove(m2)

    return None


def get_all_combinations(hand, flop, turn, river):
    all_cards = hand+ flop+ turn+ river
    
    
    return list(combinations(all_cards, 5))


def find_better(hand_1, hand_2):
    ev_1 = evaluate_hand(hand_1)
    ev_2 = evaluate_hand(hand_2)
    if ev_1[0] > ev_2[0]:
        return hand_1
    
    if ev_1[0] < ev_2[0]:
        return hand_2
    
    if ev_1[1] is not None or ev_2[1] is not None:
        high_cards1 = sorted(ev_1[1], reverse=True)
        high_cards2 = sorted(ev_2[1], reverse=True)

        for h1, h2 in zip(high_cards1, high_cards2):
            if h1 > h2:
                return hand_1
            
            if h1 < h2:
                return hand_2

    return compare_highest_card(hand_1, hand_2)


def select_best(hand, flop, turn, river):
    combs = get_all_combinations(hand, flop, turn, river)

    best = combs[0]
    for comb in combs:
        if comb != best:
            new_best = find_better(comb, best)
            if new_best is not None:
                best = new_best
   
    return list(best)

def print_pairs(p1_hand, p2_hand, better):

    p1_vals = [s+str(v) for s, v in p1_hand]
    p2_vals = [s+str(v) for s, v in p2_hand]
    print(p1_vals, p2_vals, 1 if better == p1_hand else 2)

def calculate_chances(player1_hand, player2_hand, flop, turn):
    deck = deepcopy(DECK)
    for card in player1_hand:
        deck.remove(card)
    for card in player2_hand:
        deck.remove(card)
    for card in flop:
        deck.remove(card)
    for card in turn:
        deck.remove(card)
    
    p1_wins = 0
    p2_wins = 0
    draws = 0

    for river in deck:
        river_as_list = []
        river_as_list.append(river)
        
        best_p1 = select_best(player1_hand, flop, turn, river_as_list)
        best_p2 = select_best(player2_hand, flop, turn, river_as_list)
        better = find_better(best_p1, best_p2)
        
        
        if better == best_p1:
            p1_wins +=1
        if better == best_p2:
            p2_wins +=1
        if better == None:
            draws += 1
    
    return p1_wins/44, p2_wins/44, draws/44


if __name__ == '__main__':
    pass
    # assert is_two_pairs([('S', 4), ('S', 8), ('C', 12), ('S', 12), ('H', 4)]) == (True, (12, 4))
    # assert is_two_pairs([('D', 2), ('H', 3), ('D', 3), ('C', 6), ('S', 6)]) == (True, (6, 3))
    # assert is_two_pairs([('D', 2), ('C', 2), ('S', 13), ('D', 13), ('C', 10)]) == (True, (13, 2))
    # assert is_two_pairs([('H', 6), ('C', 13), ('H', 13), ('C', 10), ('S', 10)]) == (True, (13, 10))
    # assert is_two_pairs([('H', 7), ('C', 8), ('H', 3), ('D', 7), ('S', 3)]) == (True, (7, 3))
    # assert is_two_pairs([('H', 5), ('C', 5), ('H', 2), ('C', 2), ('D', 12)]) == (True, (5, 2))
    # assert is_two_pairs([('D', 6), ('C', 5), ('H', 5), ('D', 14), ('H', 14)]) == (True, (14, 5))
    # assert is_two_pairs([('D', 4), ('D', 3), ('D', 5), ('C', 3), ('C', 4)]) == (True, (4, 3))
    # assert is_two_pairs([('S', 10), ('D', 4), ('S', 12), ('C', 12), ('S', 4)]) == (True, (12, 4))
    # assert is_two_pairs([('H', 3), ('H', 7), ('S', 3), ('D', 14), ('D', 7)]) == (True, (7, 3))
    # assert is_two_pairs([('C', 2), ('H', 4), ('D', 7), ('S', 7), ('H', 2)]) == (True, (7, 2))
    # assert is_two_pairs([('D', 10), ('C', 11), ('D', 3), ('H', 10), ('H', 3)]) == (True, (10, 3))
    # assert is_two_pairs([('C', 4), ('S', 6), ('C', 9), ('H', 6), ('D', 4)]) == (True, (6, 4))



    # p1_hand = [('H', 7), ('D', 6), ('S', 14), ('H', 14), ('H', 6)]
    # p2_hand = [('H', 3), ('C', 12), ('D', 14), ('S', 14), ('D', 3)]
    # print(find_better(p1_hand, p2_hand))
    # player1_hand, player2_hand, flop, turn = generate_setup()
    # print("PLAYER 1:", player1_hand)
    # print(is_royal_flush(player1_hand))

    # print("PLAYER 2:", player2_hand)
    # print("FLOP:", flop)
    # print("TURN:", turn)

    # p1_win, p2_win, draw = calculate_chances(
    #     player1_hand, player2_hand, flop, turn)

    # print("PLAYER 1 has a {} chance of winning".format(p1_win))
    # print("PLAYER 2 has a {} chance of winning".format(p2_win))
    # print('There\'s a {} chance of a draw'.format(draw))
