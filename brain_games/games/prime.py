#!/usr/bin/env python
"""Brain Prime Functions."""


from brain_games.engine import generate_number


def make_correct_answer():
    number = generate_number(min_number=1, max_number=21)
    question = 'Question: {0}'.format(number)
    if number == 1:
        return "no", question
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return "no", question
    return "yes", question
