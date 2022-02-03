#!/usr/bin/env python
"""Brain-Calc Functions."""


from random import choice
from operator import add, sub, mul
from brain_games.engine import generate_number


def make_correct_answer():
    num1 = generate_number(min_number=1, max_number=12)
    num2 = generate_number(min_number=1, max_number=12)
    operator, op_symbol = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    correct_answer = operator(num1, num2)
    question = ('Question: {0} {1} {2}'.format(num1, op_symbol, num2))
    return str(correct_answer), question
