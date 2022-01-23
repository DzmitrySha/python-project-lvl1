#!/usr/bin/env python
"""Brain-GCD Game."""


from random import randint
from math import gcd

from brain_games.scripts.game_scripts import welcome_user, game_logic


def get_correct_answer():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    print('Question: {0} {1}'.format(num1, num2))
    correct_answer = gcd(num1, num2)
    return str(correct_answer)


def main():
    """Start the "Brain-GCD Game"."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_logic(name, get_correct_answer)


if __name__ == '__main__':
    main()
