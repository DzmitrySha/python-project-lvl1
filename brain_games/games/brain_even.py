#!/usr/bin/env python
"""Brain-Even Game."""


from random import randint

from brain_games.scripts.game_scripts import welcome_user, game_logic


def get_correct_answer():
    start, end = 1, 99
    number = randint(start, end)
    print('Question: {0}'.format(number))
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    """Start the "Brain-Even Game"."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_logic(name, get_correct_answer)


if __name__ == '__main__':
    main()
