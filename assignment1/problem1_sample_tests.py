from copy import deepcopy

from os import listdir
from os.path import join, basename
from random import choice, randint

import problem1 as impl


sample1 = {('Daniel', 2.0): [(20, 'slow', 'card'), (3, 'quick', 'card'), (30, 'slow', 'cash'), (17, 'normal', 'card')], ('Katka', 1.5): [(13, 'slow', 'cash'), (24, 'normal', 'card')], ('Robo', 1.0): [(5, 'normal', 'cash'), (11, 'quick', 'card'), (8, 'slow', 'card')], ('Sandra', 1.25): [(38, 'slow', 'cash')]}
sample2 = {('Martin', 1.0): [(32, 'normal', 'cash'), (25, 'quick', 'card'), (46, 'slow', 'card'), (30, 'normal', 'card'), (20, 'quick', 'cash'), (19, 'normal', 'card'), (8, 'slow', 'cash'), (39, 'normal', 'card')], ('Sara', 3.0): [(9, 'normal', 'card'), (36, 'normal', 'cash'), (7, 'quick', 'card'), (14, 'normal', 'card'), (17, 'quick', 'card'), (34, 'quick', 'card'), (46, 'normal', 'cash'), (12, 'slow', 'cash'), (15, 'normal', 'cash')], ('Sandra', 2.0): [(10, 'slow', 'card'), (21, 'slow', 'card'), (46, 'slow', 'card'), (17, 'slow', 'cash'), (9, 'quick', 'cash'), (29, 'normal', 'cash')]}
sample3 = {('Ivka', 1.5): [(15, 'normal', 'card'), (34, 'normal', 'card'), (17, 'normal', 'cash'), (3, 'normal', 'card'), (6, 'normal', 'card')], ('Sara', 2.75): [(19, 'quick', 'card'), (31, 'quick', 'cash')], ('Eva', 1.0): [(28, 'slow', 'cash'), (3, 'quick', 'card'), (32, 'slow', 'cash'), (38, 'quick', 'card'), (6, 'normal', 'cash'), (38, 'quick', 'cash'), (41, 'quick', 'cash'), (13, 'quick', 'card')], ('Peter', 1.75): [(20, 'normal', 'cash'), (20, 'normal', 'card'), (6, 'normal', 'cash'), (36, 'quick', 'cash'), (11, 'slow', 'card'), (35, 'quick', 'card'), (17, 'slow', 'card'), (36, 'normal', 'card'), (28, 'slow', 'card')], ('Nika', 2.25): [(22, 'normal', 'card'), (35, 'normal', 'card'), (21, 'normal', 'card'), (33, 'quick', 'cash'), (12, 'quick', 'cash'), (4, 'quick', 'cash'), (36, 'normal', 'cash')]}
sample4 = {('Sandra', 2.25): [(7, 'quick', 'card'), (17, 'quick', 'card'), (42, 'normal', 'cash'), (23, 'normal', 'card'), (21, 'quick', 'card'), (35, 'quick', 'cash'), (27, 'quick', 'card'), (10, 'quick', 'card'), (5, 'slow', 'card')], ('Livia', 3.0): [(8, 'normal', 'cash'), (13, 'quick', 'cash'), (15, 'slow', 'cash'), (29, 'slow', 'cash'), (15, 'normal', 'card'), (29, 'quick', 'card'), (32, 'slow', 'card')], ('Nika', 2.0): [(38, 'normal', 'card'), (17, 'slow', 'card'), (21, 'quick', 'card'), (8, 'normal', 'cash'), (30, 'normal', 'cash'), (31, 'quick', 'card'), (7, 'slow', 'cash'), (27, 'slow', 'card'), (10, 'slow', 'cash'), (23, 'quick', 'card')], ('Robo', 0.75): [(49, 'slow', 'card'), (10, 'slow', 'cash')], ('Ivka', 1.5): [(47, 'normal', 'card'), (3, 'quick', 'cash'), (42, 'slow', 'card'), (15, 'quick', 'card'), (11, 'quick', 'cash'), (45, 'slow', 'cash'), (19, 'slow', 'card')]}
sample5 = {('Robo', 1.5): [(15, 'slow', 'card'), (41, 'normal', 'card'), (12, 'normal', 'cash'), (32, 'slow', 'card')], ('Kika', 1.25): [(47, 'quick', 'card')], ('Maria', 1.0): [(34, 'quick', 'card'), (41, 'normal', 'cash'), (5, 'normal', 'cash'), (34, 'quick', 'cash'), (35, 'slow', 'card'), (4, 'normal', 'cash'), (29, 'quick', 'card'), (20, 'normal', 'card'), (35, 'quick', 'cash')], ('Sara', 1.75): [(37, 'quick', 'cash'), (7, 'normal', 'cash'), (43, 'slow', 'cash')], ('Pavol', 1.25): [(39, 'normal', 'cash'), (31, 'quick', 'cash'), (12, 'quick', 'card')], ('Pavol', 2.25): [(9, 'slow', 'cash'), (29, 'normal', 'cash')], ('Robo', 2.25): [(31, 'slow', 'card'), (3, 'quick', 'card'), (26, 'quick', 'cash')], ('Pavol', 1.0): [(29, 'quick', 'card')]}

SAMPLES_DIR = "samples"

test_file_paths = [join(SAMPLES_DIR, x) for x in listdir(SAMPLES_DIR)]
# correct for problem 1
solutions = [sample1, sample2, sample3, sample4, sample5]


def test_load_queue_data():
    """
    Unit test for problem 1 - implementing load_queue_data
    """

    test_file_path = choice(test_file_paths)
    try:
        student_result = impl.load_queue_data(test_file_path)
    except AttributeError:
        print("Could not find load_queue_data")
        return
    except:
        print("Could not execute student solution - load_queue_data")
        return

    # first we check the type of the result
    print("Problem 1 - testing {}".format(basename(test_file_path)))
    print("Problem 1 - Checking return type:")
    if type(student_result) != dict:
        print("FAILURE: test_load_queue_data()")
        print("\tUnexpected return type", type(student_result),
              "(expected dict)")
        return
    else:
        print("PASSED: got dict")

    # testing type and form of keys
    print("Problem 1 - Checking keys in result:")
    for key in student_result.keys():
        if type(key) != tuple:
            print("FAILURE: load_queue_data")
            print("\tWrong key type: expected tuple, got {}".format(type(key)))
            return
        if len(key) != 2:
            print("FAILURE: load_queue_data")
            print("\tWrong key length: expected 2, got {}".format(len(key)))
            return
        if type(key[0]) != str or type(key[1]) != float:
            print("FAILURE: load_queue_data")
            print("\tWrong key element types: expected (string, float), got ({}, {})".format(type(key[0]), type(key[1])))
            return

    print("PASSED: all keys are tuples of length 2")

    # testing type and form of values
    print("Problem 1 - Checking values in result:")
    for value in student_result.values():
        if type(value) != list:
            print("FAILURE: load_queue_data")
            print("\tWrong value type: expected list, got {}".format(type(value)))
            return
        for elem in value:
            if type(elem) != tuple:
                print("FAILURE: load_queue_data")
                print("\tWrong value element type: expected tuple, got {}".format(type(elem)))
                return
            if len(elem) != 3:
                print("FAILURE: load_queue_data")
                print("\tWrong value element length: expected 3, got {}".format(len(elem)))
                return
            if type(elem[0]) != int or type(elem[1]) != str or type(elem[2]) != str:
                print("FAILURE: load_queue_data")
                print("\tWrong value element types: expected (int, string, string), got ({}, {}, {})".format(type(elem[0]), type(elem[1]), type(elem[2])))
                return

    print("PASSED: all values are lists of tuples of length 3")

    print("Problem 1 - Checking if correct data was loaded")
    data_loaded_correctly = True
    for i, test_file_path in enumerate(test_file_paths):
        if impl.load_queue_data(test_file_path) != solutions[i]:
            print("FAILURE: load_queue_data")
            print("\tIncorrectly loaded data for {}".format(basename(test_file_path)))
            data_loaded_correctly = False

    if data_loaded_correctly:
        print("PASSED: all data loaded correctly")


# correct for problem 2
customer_times = [[22, 8, 50, 19], [39, 27], [22, 18, 16], [69]]


def test_calculate_customer_time():
    error = False
    print("Problem 2 - testing correct calculation")
    i = 0
    for cashier, queue in sample1.items():
        cashier_speed = cashier[1]
        for customer_id, customer in enumerate(queue):
            try:
                student_answer = impl.calculate_customer_time(cashier_speed, deepcopy(customer))
            except:
                print("FAILURE: could not run student solution")
                return

            if type(student_answer) != int:
                print("FAILURE: test_calculate_customer_time()")
                print("\tIncorrect return type: expected int, got {}".format(type(student_answer)))
                return

            correct = customer_times[i][customer_id]
            if student_answer != correct:
                print("FAILURE: test_calculate_customer_time()")
                print("\tIncorrectly calculated customer time. Expected {}, got {}".format(correct, student_answer))
                error = True

        i += 1

    if not error:
        print("PASSED: customer times calculated correctly")


# correct for problem 3
queue_solutions = ['Robo', 'Sandra', 'Sara', 'Robo', 'Pavol']


def test_choose_queue():
    error = False
    print("Problem 3 - testing correct queue selection")
    for i, data in enumerate(solutions):
        try:
            student_answer = impl.choose_queue(deepcopy(data))
        except:
            print("FAILURE: could not run student solution")
            return

        if type(student_answer) != str:
            print("FAILURE: test_choose_queue()")
            print("\tIncorrect return type: expected str, got {}".format(type(student_answer)))
            return

        correct = queue_solutions[i]
        if student_answer != correct:
            print("FAILURE: test_calculate_customer_time()")
            print("\tIncorrectly selected queue. Expected {}, got {}".format(correct, student_answer))
            error = True

    if not error:
        print("PASSED: queues chosen correctly")


# correct for problem 4
where_to_send_customers = [(20, 'quick', 'cash'), (6, 'normal', 'card')]
where_to_send_results = [['Katka', 'Sara', 'Ivka', 'Sandra', 'Robo'], ['Katka', 'Sara', 'Ivka', 'Sandra', 'Robo']]


def test_where_to_send():
    print("Problem 4 - testing correct queue allocation")
    error = False
    for c_i, customer in enumerate(where_to_send_customers):
        for s_i, sample in enumerate(solutions):
            try:
                student_answer = impl.where_to_send(deepcopy(sample), deepcopy(customer))
            except:
                print("FAILURE: could not run student solution")
                return

            if type(student_answer) != str:
                print("FAILURE: test_where_to_send()")
                print("\tIncorrect return type: expected str, got {}".format(type(student_answer)))
                return

            correct = where_to_send_results[c_i][s_i]
            if student_answer != correct:
                print("FAILURE: test_where_to_send()")
                print("\tIncorrectly allocated queue. Expected {}, got {}".format(correct, student_answer))
                error = True

    if not error:
        print("PASSED: customers allocated correctly")


# correct for problem 5
test_cashiers = [('Robo', 2), ('Dano', 1.25)]
test_save_times = [10, 30]
use_cashier_results = [
    [[True, True, True, True, True], [False, True, False, False, True]],
    [[True, True, True, True, True], [False, True, False, False, True]]]


def test_should_use_cashier():
    print("Problem 5 - testing cashier employment")
    error = False

    for c_i, cashier in enumerate(test_cashiers):
        for t_i, save_time in enumerate(test_save_times):
            for s_i, sample in enumerate(solutions):
                try:
                    student_answer = impl.should_use_cashier(
                        deepcopy(cashier), deepcopy(sample), save_at_least=save_time)
                except:
                    print("FAILURE: could not run student solution")
                    return

                if type(student_answer) != bool:
                    print("FAILURE: test_should_use_cashier()")
                    print("\tIncorrect return type: expected bool, got {}".format(type(student_answer)))
                    return

                correct = use_cashier_results[c_i][t_i][s_i]
                if student_answer != correct:
                    # print(cashier, sample, save_time)
                    # print(student_answer)
                    # print(correct)
                    print("FAILURE: test_should_use_cashier()")
                    print("\tIncorrectly used cashier. Expected {}, got {}".format(correct, student_answer))
                    return

    if not error:
        print("PASSED: cashiers employed correctly")


def test_student_solution():
    print("Testing problem 1 - load_queue_data")
    test_load_queue_data()
    print()

    print("Testing problem 2 - calculate_customer_time")
    test_calculate_customer_time()
    print()

    print("Testing problem 3 - choose_queue")
    test_choose_queue()
    print()

    print("Testing problem 4 - where_to_send")
    test_where_to_send()
    print()

    print("Testing problem 5 - should_use_cashier")
    test_should_use_cashier()
    print()


if __name__ == '__main__':
    test_student_solution()
