#!/usr/bin/env python
"""Brain Progression Functions."""


from random import randint


MIN_LENGTH = 4
MAX_LENGTH = 10

MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 20

MIN_STEP = 1
MAX_STEP = 11


def make_progression():
    progression_len = randint(MIN_LENGTH, MAX_LENGTH)
    progression_step = randint(MIN_STEP, MAX_STEP)
    first_num = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    progression = [first_num, ]
    for i in range(progression_len):
        progression.append(first_num + progression_step)
        first_num += progression_step
    return progression


def make_correct_answer():
    progression = make_progression()
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    list_progression = ' '.join(map(str, progression))
    print('Question: {0}'.format(list_progression))
    return str(correct_answer)
