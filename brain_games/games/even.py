#!/usr/bin/env python
"""Brain-Even Functions."""


from brain_games.engine import generate_number


def make_correct_answer():
    number = generate_number()
    question = ('Question: {0}'.format(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
