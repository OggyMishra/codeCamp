#!/bin/python3

import math
import os
import random
import re
import sys

# region Write a program to calculate the 40th number on the fibonacci sequence.
# e.g 1, 1, 2, 3, 5, 8, 13, 21
# so 7 the no is 13.

# region Iterative solution to print fib sequence


# def fib(n):
#     output = []
#     for i in range(1, n+1):
#         if i <= 2:
#             output += [1]
#         else:
#             output += [output[-1]+output[-2]]
#
#     print(output)
# endregion

# region recursive solution


def fib_seq(n):
    if n <= 2:
        return 1
    else:
        return fib_seq(n - 1) + fib_seq(n - 2)


def fib(n):
    for i in range(1, n+1):
        print(fib_seq(i))

# endregion

# endregion

# region Count the number of different ways to move through a 6 * 9 grid

# endregion

# region Given a set of coins, how can we make 27 cents in the least number of coins ?

# endregion

# region Given a set of substrings, what are the possible ways to construct the string 'potentpot' ?

# endregion

if __name__ == '__main__':
    fib(25)
