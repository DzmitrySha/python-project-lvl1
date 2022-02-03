#!/usr/bin/env python
"""Brain-GCD Functions."""


from math import gcd
from brain_games.engine import generate_number


def make_correct_answer():
    num1 = generate_number()
    num2 = generate_number()
    question = 'Question: {0} {1}'.format(num1, num2)
    correct_answer = gcd(num1, num2)
    return str(correct_answer), question
