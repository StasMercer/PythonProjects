import pandas as pd
import traceback
import problem2 as impl


def load_sample_eval_data():
    return pd.read_csv(
        'eval.csv', header=0, sep=';', converters={'hand': eval})


def load_sample_pick_data():
    return pd.read_csv(
        'pick.csv', header=0, sep=';', converters={
            'hand1': eval, 'hand2': eval, 'winner': eval
        })


def load_sample_select_data():
    return pd.read_csv(
        'select.csv', header=0, sep=';', converters={
            'available': eval, 'hand': eval
        })


def load_sample_chances_data():
    return pd.read_csv(
        'chances.csv', header=0, sep=';', converters={
            'hand_1': eval, 'hand_2': eval, 'flop': eval, 'turn': eval
        })


def test_is_royal_flush(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['royal_flush']

        try:
            student_result, card_vals = impl.is_royal_flush(hand)
        except AttributeError:
            print('Could not find is_royal_flush')
            return
        except:
            print('Could not execute student solution - is_royal_flush')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_royal_flush()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Royal Flush evaluated correctly")


def test_is_straight_flush(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['straight_flush']

        try:
            student_result, card_vals = impl.is_straight_flush(hand)
        except AttributeError:
            print('Could not find is_straight_flush')
            return
        except:
            print('Could not execute student solution - is_straight_flush')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_straight_flush()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Straight Flush evaluated correctly")


def test_is_four_of_a_kind(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['four_of_a_kind']

        try:
            student_result, card_vals = impl.is_four_of_a_kind(hand)
        except AttributeError:
            print('Could not find is_four_of_a_kind')
            return
        except:
            print('Could not execute student solution - is_four_of_a_kind')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_four_of_a_kind()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Four of a Kind evaluated correctly")


def test_is_full_house(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['full_house']

        try:
            student_result, card_vals = impl.is_full_house(hand)
        except AttributeError:
            print('Could not find is_full_house')
            return
        except:
            print('Could not execute student solution - is_full_house')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_full_house()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Full House evaluated correctly")


def test_is_flush(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['flush']

        try:
            student_result, card_vals = impl.is_flush(hand)
        except AttributeError:
            print('Could not find is_flush')
            return
        except:
            print('Could not execute student solution - is_flush')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_flush()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Flush evaluated correctly")


def test_is_straight(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['straight']

        try:
            student_result, card_vals = impl.is_straight(hand)
        except AttributeError:
            print('Could not find is_straight')
            return
        except:
            print('Could not execute student solution - is_straight')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_straight()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Straight evaluated correctly")


def test_is_three_of_a_kind(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['three_of_a_kind']

        try:
            student_result, card_vals = impl.is_three_of_a_kind(hand)
        except AttributeError:
            print('Could not find is_three_of_a_kind')
            return
        except:
            print('Could not execute student solution - is_three_of_a_kind')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_three_of_a_kind()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Three of a Kind evaluated correctly")


def test_is_two_pairs(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['two_pairs']

        try:
            student_result, card_vals = impl.is_two_pairs(hand)
        except AttributeError:
            print('Could not find is_two_pairs')
            return
        except:
            print('Could not execute student solution - is_two_pairs')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_two_pairs()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Two Pairs evaluated correctly")


def test_is_pair(data):
    for idx, row in data.iterrows():
        hand = row['hand']
        correct = row['pair']

        try:
            student_result, card_vals = impl.is_pair(hand)
        except AttributeError:
            print('Could not find is_pair')
            return
        except:
            print('Could not execute student solution - is_pair')
            return

        if type(student_result) != bool or (type(card_vals) != tuple and card_vals is not None):
            print('FAIURE: test_is_royal_flush()')
            print('\tWrong output_type. Expected (bool, tuple), got ({}, {})'.format(type(student_result), type(card_vals)))
            return

        if student_result != correct:
            print("FAILURE: test_is_pair()")
            print("\tWrong result for hand {}. Expected {}, got {}".format(
                hand, correct, student_result))
            return

    print("PASSED: Pair evaluated correctly")


def test_problem_2(data):
    for idx, row in data.iterrows():
        p1_hand = row['hand1']
        p2_hand = row['hand2']
        correct = row['winner']

        try:
            student_result = impl.find_better(p1_hand, p2_hand)

            p1_val = impl.evaluate_hand(p1_hand)
            p2_val = impl.evaluate_hand(p2_hand)

            if p1_val == p2_val:
                try:
                    student_comparison = impl.compare_highest_card(p1_hand, p2_hand)
                except AttributeError:
                    print('Could not find compare_highest_card')
                    return
                except:
                    print('Could not execute student solution - compare_highest_card')
                    return

                if student_comparison != correct:
                    print("FAILURE: test_problem_2() - error in compare_highest_card")
                    print("\tWrong hand selected from {} and {}. Expected {}, got {}".format(
                        p1_hand, p2_hand, correct, student_comparison))
        except AttributeError:
            print('Could not find find_better')
            return
        except:
            print('Could not execute student solution - find_better')
            return

        if student_result != correct:
            print("FAILURE: test_problem_2() - error in find_better")
            print("\tWrong hand selected from {} and {}. Expected {}, got {}".format(
                p1_hand, p2_hand, correct, student_result))
            return

    print("PASSED: Picked winning hands correctly")


def test_get_all_combinations(data):
    for idx, row in data.iterrows():
        pool = row['available']
        hand = pool[:2]
        flop = pool[2:5]
        turn = [pool[5]]
        river = [pool[6]]

        try:
            student_combinations = impl.get_all_combinations(
                hand, flop, turn, river)
        except AttributeError:
            print('Could not find get_all_combinations')
            return
        except:
            print('Could not execute student solution - get_all_combinations')
            return

        if type(student_combinations) != list:
            print("FAILURE: test_get_all_combinations()")
            print("\tWrong return type. Expected list, got {}".format(type(student_combinations)))
            return

        if len(student_combinations) != 21:
            print("FAILURE: test_get_all_combinations()")
            print("\tYour solution did not find all combinations. Expected 21, got {}".format(len(student_combinations)))
            return

        for combination in student_combinations:
            if len(combination) != 5:
                print("FAILURE: test_get_all_combinations()")
                print("\tWrong combination length. {} has {} cards, expected 5".format(combination, len(combination)))
                return

            for elem in combination:
                if type(elem) != tuple:
                    print("FAILURE: test_get_all_combinations()")
                    print("\tWrong return type. Expected list of tuples, got list of {}".format(type(elem)))
                    return
                if len(elem) != 2:
                    print("FAILURE: test_get_all_combinations()")
                    print("\tWrong return type. Expected list of tuples with 2 values, got list of tuples with {} values".format(len(elem)))
                    return
                if type(elem[0]) != str or type(elem[1]) != int:
                    print("FAILURE: test_get_all_combinations()")
                    print("\tWrong return type. Tuples should have values string and int, got {} and {} ({})".format(type(elem[0]), type(elem[1]), elem))
                    return

            if len(set(combination)) != 5:
                print("FAILURE: test_get_all_combinations()")
                print("\tCombination {} has duplicit values".format(combination))
                return

    print("PASSED: generated combinations correctly")


def test_select_best(data):
    for idx, row in data.iterrows():
        pool = row['available']
        hand = pool[:2]
        flop = pool[2:5]
        turn = [pool[5]]
        river = [pool[6]]
        correct = row['hand']

        try:
            student_result = impl.select_best(
                hand, flop, turn, river)
        except AttributeError:
            print('Could not find select_best')
            return
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            print('Could not execute student solution - select_best')
            return

        if student_result != correct:
            print("FAILURE: test_select_best()")
            print("\tWrong hand selected from available cards {}. Expected {}, got {}".format(pool, correct, student_result))
            return

    print("PASSED: selected best combination from available cards")


def test_calculate_chances(data):
    for idx, row in data.iterrows():
        p1_hand = row['hand_1']
        p2_hand = row['hand_2']
        flop = row['flop']
        turn = row['turn']
        p1_win = row['p1_win']
        p2_win = row['p2_win']
        draw = row['draw']

        try:
            s_p1_win, s_p2_win, s_draw = impl.calculate_chances(
                p1_hand, p2_hand, flop, turn)
        except AttributeError:
            print('Could not find calculate_chances')
            return
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            print('Could not execute student solution - calculate_chances')
            return

        if abs(s_p1_win - p1_win) > 0.00000001:
            print("FAILURE: test_calculate_chances()")
            print("\tWrong Play 1 winning chance. Expected {}, got {}".format(p1_win, s_p1_win))
            return
        if abs(s_p2_win - p2_win) > 0.00000001:
            print("FAILURE: test_calculate_chances()")
            print("\tWrong Play 2 winning chance. Expected {}, got {}".format(p2_win, s_p2_win))
            return
        if abs(s_draw - draw) > 0.00000001:
            print("FAILURE: test_calculate_chances()")
            print("\tWrong draw chance. Expected {}, got {}".format(draw, s_draw))
            return

    print("PASSED: correctly calculated outcome chances")


def test_student_solution():
    sample_eval_data = load_sample_eval_data()
    sample_pick_data = load_sample_pick_data()
    sample_select_data = load_sample_select_data()
    sample_chances_data = load_sample_chances_data()

    # PROBLEM 1 #
    print("Testing problem 1.1 - is_royal_flush")
    test_is_royal_flush(sample_eval_data)
    print()

    print("Testing problem 1.2 - is_straight_flush")
    test_is_straight_flush(sample_eval_data)
    print()

    print("Testing problem 1.3 - is_four_of_a_kind")
    test_is_four_of_a_kind(sample_eval_data)
    print()

    print("Testing problem 1.4 - is_full_house")
    test_is_full_house(sample_eval_data)
    print()

    print("Testing problem 1.5 - is_flush")
    test_is_flush(sample_eval_data)
    print()

    print("Testing problem 1.6 - is_straight")
    test_is_straight(sample_eval_data)
    print()

    print("Testing problem 1.7 - is_three_of_a_kind")
    test_is_three_of_a_kind(sample_eval_data)
    print()

    print("Testing problem 1.8 - is_two_pairs")
    test_is_two_pairs(sample_eval_data)
    print()

    print("Testing problem 1.9 - is_pair")
    test_is_pair(sample_eval_data)
    print()

    # PROBLEM 2 #
    print("Testing problem 2 - compare_highest and find_better")
    test_problem_2(sample_pick_data)
    print()

    # PROBLEM 3 #
    print("Testing problem 3.1 - get_all_combinations")
    test_get_all_combinations(sample_select_data)
    print()

    print("Testing problem 3.2 - select_best")
    test_select_best(sample_select_data)
    print()

    # PROBLEM 4 #
    print("Testing problem 4 - calculate_chances")
    test_calculate_chances(sample_chances_data)
    print()


if __name__ == '__main__':
    test_student_solution()
