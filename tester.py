import random
import sys
import os

EXECUTABLE_NAME = "project2"

class Option:
    def __init__(self, weight, function):
        self.weight = weight
        self.function = function

options = []
routes = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13"]
stops = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13"]

connection_origin = "p1"
connection_destiny = "p2"

original_stdout = sys.stdout

curr_route = "c1"

first_connection_var = True

# c
def c(chosen_stop, chosen_route, first):
    return "c"

# c c1 arg
def c_1(chosen_stop, chosen_route, first):
    return f"c {chosen_route}"

# c c1 inv
def c_2(chosen_stop, chosen_route, first):
    inverso_list = ["inv", "inve", "inver", "invers", "inverso"]
    inverso_list_index = random.randint(0, 4)
    return f"c {chosen_route} {inverso_list[inverso_list_index]}"

# p
def p(chosen_stop, chosen_route, first):
    return "p"

# p p1
def p_1(chosen_stop, chosen_route, first):
    return f"p {chosen_stop}"

# p p1 1 1
def p_2(chosen_stop, chosen_route, first):
    return f"p {chosen_stop} 1 1"

# l c1 p1 p2 1 1
def l(chosen_stop, chosen_route, first):
    global connection_origin
    global connection_destiny
    rand_choice = random.randint(1, 2)
    # Adding to the start
    if (first):
        phrase = f"l {curr_route} {connection_origin} {chosen_stop} 1 1"
        connection_destiny = chosen_stop
        return phrase

    elif (rand_choice == 1):
        phrase = f"l {curr_route} {chosen_stop} {connection_origin} 1 1"
        connection_origin = chosen_stop
        return phrase

    # Adding to the end
    elif (rand_choice == 2):
        phrase = f"l {curr_route} {connection_destiny} {chosen_stop} 1 1"
        connection_destiny = chosen_stop
        return phrase

# i
def i(chosen_stop, chosen_route, first):
    return "i"

# r c1
def r(chosen_stop, chosen_route, first):
    return f"r {chosen_route}"

# e p1
def e(chosen_stop, chosen_route, first):
    return f"e {chosen_stop}"

# a
def a(chosen_stop, chosen_route, first):
    return "a"

option_list = [
Option(0.1, c), Option(0.1, c_1), Option(0.1, c_2),
Option(0.1, p), Option(0.1, p_1),Option(0.1, p_2),
Option(0.1, l), Option(0.005, i), Option(0.075, r),
Option(0.075, e), Option(0.0005, a)
]

def select_random_option():
    global first_connection_var
    global curr_route
    global num
    total_weight = sum(option.weight for option in option_list)
    rand = random.uniform(0, total_weight)
    current_weight = 0

    for option in option_list:
        current_weight += option.weight
        if rand <= current_weight:
            chosen_option = option
            break
    
    chosen_stop = stops[random.randint(0, 12)]
    chosen_route = routes[random.randint(0, 12)]

    option_to_print = chosen_option.function(chosen_stop, chosen_route, first_connection_var)
    if (chosen_option.function.__name__ == "l"):
        if first_connection_var == True:
            chosen_option.weight = 1.5
            first_connection_var = False
        else:
            if chosen_option.weight > 0.1:
                chosen_option.weight -= 0.1
    else:
        curr_route = chosen_route
        first_connection_var = True
    # if (my_option.function.__name__ == "l")
    print(option_to_print)
    
original_stdout = sys.stdout

with open('segfault_tester.txt', 'w') as f:
    # Redirect all stdout to the file
    sys.stdout = f
    for i in range(len(stops)):
        print(f"p {stops[i]} 1 1")

    for i in range(len(routes)):
        print(f"c {routes[i]}")

    for i in range(1000):
        select_random_option()
    print("q")

if (os.system(f'./{EXECUTABLE_NAME} < ./segfault_tester.txt') != 0):
    with open('segfault_tester.txt', 'r+') as f:
        lines = []
        for line in f:
            lines.append(line.strip())

    with open("segfault_tester.txt", "w") as f:
        sys.stdout = f
        print("q")

    total_num = 0
    lines_len = len(lines)

    while (os.system(f'./{EXECUTABLE_NAME} < ./segfault_tester.txt') == 0):
        with open('segfault_tester.txt', 'w') as f:
            sys.stdout = f
            for i in range(total_num):
                print(lines[i])
            total_num += 1
            print("q")

    middle_lines = lines[:total_num - 2]
    last_lines = [lines[total_num - 2], "q"]

    index_to_remove = -1
    middle_lines_mod = middle_lines[:index_to_remove]

    for i in range(len(middle_lines)):

        with open('segfault_tester.txt', 'w') as f:
            sys.stdout = f

            if (index_to_remove != -1):
                middle_lines_mod = middle_lines[:index_to_remove] + middle_lines[index_to_remove+1:]
            else:
                middle_lines_mod = middle_lines[:index_to_remove]

            for item in middle_lines_mod:
                print(item)

            for item in last_lines:
                print(item)

            index_to_remove -= 1

        if (os.system(f'./{EXECUTABLE_NAME} < ./segfault_tester.txt') != 0):
            middle_lines = middle_lines_mod
            index_to_remove += 1
else:
    sys.stdout = original_stdout
    print("\nNo errors were found")
    print("Please try again until the program starts optimizing a test for you")