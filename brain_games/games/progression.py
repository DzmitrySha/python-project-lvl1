"""Brain Progression Game."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression(progression_len,
                     min_step, max_step,
                     min_first_num, max_first_num):
    """Generate arithmetic progression."""
    first_num = randint(min_first_num, max_first_num)
    progression_step = randint(min_step, max_step)
    progression = [first_num, ]
    for i in range(progression_len):
        next_num = first_num + progression_step
        progression.append(next_num)
        first_num = next_num
    return progression


def make_question_and_correct_answer():
    """ Make game question and answer."""
    progression = make_progression(
        progression_len=10,
        min_step=1,
        max_step=10,
        min_first_num=0,
        max_first_num=20
    )
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
