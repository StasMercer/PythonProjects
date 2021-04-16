# -*- coding: utf-8 -*-

# Zadanie 1.1 - Čakáme a čakáme

# Meno: Stanislav Ivanchyk
# Spolupráca: 
# Použité zdroje:
# https://www.w3schools.com/python/python_lambda.asp
# https://www.programiz.com/python-programming/shallow-deep-copy
# Čas: 6 hodin
import math
import copy
def load_queue_data(file_path):
    # returns the queues information as a dictionary with:
    # key -- a tuple with cashier information
    # value -- a list of tuples with customer information
    res_dict = {}
    with open(file_path, 'r') as f:

        lines = f.readlines()
        current = None

        for line in lines:

            splited = line.strip().split(', ')
            
            if len(splited) == 2:
                splited[1] = float(splited[1])
                current = tuple(splited)
                res_dict[current] = []   
            elif len(splited) == 3:
                splited[0] = int(splited[0])
                res_dict[current].append(tuple(splited))
            elif current is None:
                raise RuntimeError('Cashier should be first')
            else:
                raise RuntimeError('Wrong data format, every line should have 2 or 3 values separeted by commas')

    # print(res_dict)
    return res_dict


def calculate_customer_time(cashier_speed, customer):
    # calculates the amount of time of serving a customer in seconds
    # returns an integer
    customer_type = customer[1]
    payment_type = customer[2]
    items = customer[0]
    payment_time = 5 #card default
    payment_cash_types = {"slow": 25, 'normal': 15, 'quick': 10}
    packing_time_types = {"slow": 3, 'normal': 4, 'quick': 6}

    packing_time = packing_time_types[customer_type]
    
    if payment_type == 'cash':
        payment_time = payment_cash_types[customer_type]
    


    return math.ceil(items / cashier_speed) + math.ceil(items / packing_time) + payment_time


def choose_queue(queues):
    # returns the name of the cashier whose queue the user should join
    res = ['', math.inf]

    
    for cashier, queue in queues.items():

        whole_time = sum([calculate_customer_time(cashier[1], customer) for customer in queue])
    
        if whole_time < res[1]:
            res = [cashier[0], whole_time]
        
    return res[0]

def calculate_last_time(queues):
    # returns time when last customer leave queue
    res = 0
    for cashier, queue in queues.items():
        customer_time = sum([calculate_customer_time(cashier[1], customer) for customer in queue])
        if customer_time > res:
            res = customer_time

    return res

def where_to_send(queues, customer):
    # returns the name of the cashier whose queue we should send the customer
    # to minimze overall waiting time among all queues

    #copy to prevent mutations in original dict
    new_queues = copy.deepcopy(queues)
    
    for k in new_queues:
        new_queues[k].append(customer)
    print(choose_queue(new_queues))
    return choose_queue(new_queues)


def should_use_cashier(cashier, queues, save_at_least=30):
    # determines whether it would pay off to open a new cash register
    # returns a boolean
    # -- True if the waiting time saved by opening the cash register is
    #    more than the minimal amount of time where it pays off to open it
    # -- False otherwise

    #copy to prevent mutations in original dict
    new_queues = copy.deepcopy(queues)

    no_cashier_time = calculate_last_time(new_queues)
    
    #remove last customers
    [single_queue.pop() for single_queue in new_queues.values() if len(single_queue) > 1]

    with_cashier_time = calculate_last_time(new_queues)

    saved_time = no_cashier_time - with_cashier_time
    print(no_cashier_time,  with_cashier_time, saved_time)

    return saved_time >= save_at_least


if __name__ == '__main__':
    # use this function to test your solutions at your convenience
    # should_use_cashier(('Daniel', 2.0), {('Kika', 1.25): [(10, 'slow', 'cash')], ('Daniel', 2.75): [(19, 'normal', 'cash'), (34, 'normal', 'card'), (16, 'slow', 'card'), (26, 'normal', 'card')], ('Peter', 2.25): [(29, 'quick', 'card'), (47, 'normal', 'card'), (18, 'slow', 'card'), (18, 'slow', 'card'), (46, 'slow', 'card'), (27, 'normal', 'card'), (46, 'slow', 'cash'), (8, 'slow', 'cash'), (22, 'slow', 'card'), (13, 'quick', 'cash')], ('Maria', 0.75): [(43, 'quick', 'card')], ('Laco', 2.0): [(25, 'normal', 'card'), (32, 'slow', 'cash'), (31, 'slow', 'cash'), (50, 'quick', 'cash'), (48, 'slow', 'card'), (30, 'quick', 'card')], ('Ivka', 1.75): [(12, 'slow', 'card'), (32, 'quick', 'card'), (18, 'slow', 'card'), (37, 'slow', 'cash'), (17, 'slow', 'cash'), (18, 'quick', 'cash'), (19, 'slow', 'card')], ('Robo', 2.25): [(23, 'quick', 'card'), (15, 'slow', 'cash'), (20, 'normal', 'card'), (4, 'normal', 'card'), (26, 'slow', 'cash'), (21, 'normal', 'cash')], ('Robo', 2.75): [(45, 'normal', 'card'), (18, 'slow', 'cash'), (34, 'quick', 'cash'), (9, 'slow', 'card')], ('Livia', 1.25): [(28, 'normal', 'cash'), (32, 'slow', 'cash'), (16, 'quick', 'card'), (26, 'normal', 'card'), (30, 'quick', 'card'), (20, 'normal', 'card')], ('Maria', 2.25): [(42, 'normal', 'card'), (34, 'slow', 'card')]}, 19)
    pass
    