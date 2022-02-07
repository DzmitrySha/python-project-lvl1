#!/usr/bin/env python
"""Brain Prime Functions."""


from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def make_question_and_correct_answer():
    """ Make game question and answer."""
    min_number = 1
    max_number = 21
    number = randint(min_number, max_number)
    question = str(number)
    if number == 1:
        return question, "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return question, "no"
    return question, "yes"
