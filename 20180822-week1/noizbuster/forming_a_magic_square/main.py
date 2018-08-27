#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


def gen_sum_map(flatten, balance):
    sums = [
        flatten[0] + flatten[3] + flatten[6] - balance,
        flatten[1] + flatten[4] + flatten[7] - balance,
        flatten[2] + flatten[5] + flatten[8] - balance,
        flatten[0] + flatten[1] + flatten[2] - balance,
        flatten[3] + flatten[4] + flatten[5] - balance,
        flatten[6] + flatten[7] + flatten[8] - balance
    ]
    return sums


# remove value from items of targetSet
def interpolate(i_value, t_set):
    remains = i_value
    if remains == 0:
        return t_set
    # first, remove value AMAP
    for i in range(len(t_set)):
        if t_set[i] * remains > 0 and t_set[i] <= remains:
            remains -= t_set[i]
            t_set[i] = 0
        elif t_set[i] * remains > 0 and t_set[i] > remains:
            t_set[i] -= remains
            remains = 0
    # If still there interpolate value remains, dump it
    for i in range(len(t_set)):
        if t_set[i] * remains < 0:
            t_set[i] -= remains
            remains = 0
    t_set[0] -= remains
    return t_set


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # reduce to make 1d array
    flatten = reduce(lambda x, y: x + y, s)
    # make sum map
    sum_map = gen_sum_map(flatten, 15)
    # split left hand and right hand
    l_set = sum_map[:3]
    r_set = sum_map[3:]

    # interpolating
    move = 0
    print('l:', l_set, 'r:', r_set, 'move', move)
    for i in range(len(r_set)):
        move += abs(r_set[i])
        l_set = interpolate(r_set[i], l_set)
        r_set[i] = 0
        print('l:', l_set, 'r:', r_set, 'move', move)

    for j in l_set:
        move += abs(l_set[j])
        r_set = interpolate(l_set[j], r_set)
        l_set[j] = 0
        print('l:', l_set, 'r:', r_set, 'move', move)

    return move


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []
    # i = ['4 9 2','3 5 7','8 1 5']
    # i = ['4 8 2', '4 5 7', '6 1 6']
    i = ['2 9 8', '4 2 7', '5 6 7']

    for _ in range(3):
        s.append(list(map(int, i[_].rstrip().split())))
    # print('s is', s)
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print('result:', result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
