#!/usr/bin/env python
"""Brain Progression Functions."""


from random import randrange


def make_correct_answer():
    len_min, len_max = 4, 10
    len_progression = randrange(len_min, len_max)
    max_range = 21
    start_num = randrange(max_range)
    min_step = 1
    max_step = 11
    step = randrange(min_step, max_step)
    progression = [start_num, ]
    for i in range(len_progression):
        progression.append(start_num + step)
        start_num += step
    random_index = randrange(0, len_progression + 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    list_progression = ' '.join(map(str, progression))
    print('Question: {0}'.format(list_progression))
    return str(correct_answer)
