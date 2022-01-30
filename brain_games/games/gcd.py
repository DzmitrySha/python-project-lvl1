#!/usr/bin/env python
"""Brain-GCD Functions."""


from random import randint
from math import gcd


def make_correct_answer():
    start, end = 1, 99
    num1 = randint(start, end)
    num2 = randint(start, end)
    print('Question: {0} {1}'.format(num1, num2))
    correct_answer = gcd(num1, num2)
    return str(correct_answer)
