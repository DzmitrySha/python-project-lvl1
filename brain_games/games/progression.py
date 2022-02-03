#!/usr/bin/env python
"""Brain Progression Functions."""


from brain_games.engine import generate_number

MIN_LENGTH = 4
MAX_LENGTH = 10

MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 20

MIN_STEP = 1
MAX_STEP = 11


def make_progression():
    progression_len = generate_number(MIN_LENGTH, MAX_LENGTH)
    progression_step = generate_number(MIN_STEP, MAX_STEP)
    first_num = generate_number(MIN_FIRST_NUM, MAX_FIRST_NUM)
    progression = [first_num, ]
    for i in range(progression_len):
        next_num = first_num + progression_step
        progression.append(next_num)
        first_num = next_num
    return progression


def make_correct_answer():
    progression = make_progression()
    random_index = generate_number(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    progression_list = ' '.join(map(str, progression))
    question = 'Question: {0}'.format(progression_list)
    return str(correct_answer), question
