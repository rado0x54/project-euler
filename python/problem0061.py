#!/usr/bin/env python3
"""Project Euler - Problem 61 Module"""


def get_figurate_number(nr_vertex, n):
    "Return n-th Figurative Number for vertex nr"
    # compare http://oeis.org/wiki/Figurate_numbers
    return ((nr_vertex - 2) * (n**2) - (nr_vertex - 4) * n) // 2


def generate_figurate_number(nr_vertex, a, b):
    "Return generator of figurativ numbers between [a,b["

    i = 0
    fig_nr = 0
    while fig_nr < b:
        if fig_nr >= a:
            yield fig_nr
        i += 1
        fig_nr = get_figurate_number(nr_vertex, i)


def find_cyclic_path(numberarray, pre_postfix_len, solution, pre_postfix=None):
    # Break condition: Empty Array & pre_postfix equal
    if not numberarray:
        return pre_postfix != None and pre_postfix[0] == pre_postfix[1]

    for key in numberarray:
        for i in numberarray[key]:
            cur_pre = i[:pre_postfix_len]
            cur_post = i[pre_postfix_len:]

            pre = pre_postfix[0] if pre_postfix != None else cur_pre
            step_in = pre_postfix == None or pre_postfix[1] == cur_pre

            next_numberarray = numberarray.copy()
            next_numberarray.pop(key)
            if step_in and find_cyclic_path(next_numberarray, pre_postfix_len, solution, (pre, cur_post)):
                solution.append(int(i))
                #print("FOUND!{}:{}".format(key,i))
                return True

        if pre_postfix == None:
            break  # Inital case: No need to look at any other lists

    return False


def problem61(figurate_range, nr_len):
    """Problem 61 - Cyclical figurate numbers"""

    result = []

    fig_num_array = {}
    for i in range(figurate_range[0], figurate_range[1] + 1):
        fig_num_array[i] = [str(x) for x in generate_figurate_number(
            i, 10 ** (nr_len - 1), 10 ** nr_len)]
    find_cyclic_path(fig_num_array, 2, result)


    return sum(result)


def run():
    """Default Run Method"""
    return problem61((3, 8), 4)

if __name__ == '__main__':
    print("Result: ", run())
