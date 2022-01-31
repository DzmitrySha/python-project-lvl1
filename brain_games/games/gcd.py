#!/usr/bin/env python
"""Brain-GCD Functions."""


from random import randint
from math import gcd


MIN_NUMBER = 1
MAX_NUMBER = 99


def make_correct_answer():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    print('Question: {0} {1}'.format(num1, num2))
    correct_answer = gcd(num1, num2)
    return str(correct_answer)
