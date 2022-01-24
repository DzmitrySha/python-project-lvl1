#!/usr/bin/env python
"""Brain Prime Game."""


from random import randrange


from brain_games.scripts.game_scripts import welcome_user, game_logic


def get_correct_answer():
    start, end = 1, 20
    number = randrange(start, end)
    print('Question: {0}'.format(number))
    if number == 1:
        return 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def main():
    """Start the "Brain Prime Game"."""
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    game_logic(name, get_correct_answer)


if __name__ == '__main__':
    main()
