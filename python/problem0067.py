#!/usr/bin/env python3
"""Project Euler - Problem 67 Module"""

import os


def problem67(triangle_fileloc):
    """Problem 67 - Maximum path sum II"""

    # We model tree node with dict:
    # node = { 'value':123, 'left': {}, 'right': {}, 'depth':1}

    root = {}
    cur_depth = [root]

    d = 0
    d_nodelist = []
    # read file
    with open(triangle_fileloc, 'r') as f:
        for line in f:
            d_nodelist.append(cur_depth)

            counter = 0
            next_depth = []
            for value in line.split():
                cur_depth[counter]['value'] = int(value)
                cur_depth[counter]['depth'] = d
                if not next_depth:
                    cur_depth[counter]['left'] = {}
                    next_depth.append(cur_depth[counter]['left'])
                else:
                    cur_depth[counter]['left'] = next_depth[-1]

                cur_depth[counter]['right'] = {}
                next_depth.append(cur_depth[counter]['right'])

                counter += 1

            cur_depth = next_depth
            d += 1

    # Correct Stuff
    d -= 1

    while d >= 0:
        for x in d_nodelist[d]:
            cur_max = x['value']

            if ('cur_max' in x['left'] and 'cur_max' in x['right']):
                if (x['left']['cur_max'] > x['right']['cur_max']):
                    cur_max += x['left']['cur_max']
                else:
                    cur_max += x['right']['cur_max']

            x['cur_max'] = cur_max

        d -= 1

    return root['cur_max']

FILENAME = 'problem0067.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run():
    """Default Run Method"""
    return problem67(os.path.join(__location__, FILENAME))

if __name__ == '__main__':
    print("Result: ", run())
