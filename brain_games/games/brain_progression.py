#!/usr/bin/env python
"""Brain Progression Game."""


from random import randrange


from brain_games.scripts.game_scripts import welcome_user, game_logic


def get_correct_answer():
    len_progression = randrange(4, 10)
    start_num = randrange(0, 21)
    step = randrange(1, 11)
    progression = [start_num, ]
    for i in range(len_progression):
        progression.append(start_num + step)
        start_num += step
    random_index = randrange(0, len_progression + 1)
    ask_number = progression[random_index]
    progression[random_index] = '..'
    list_progression = ' '.join(map(str, progression))
    print('Question: {0}'.format(list_progression))
    return str(ask_number)


def main():
    """Start the "Brain-Progression Game"."""
    name = welcome_user()
    print('What number is missing in the progression?')
    game_logic(name, get_correct_answer)


if __name__ == '__main__':
    main()
