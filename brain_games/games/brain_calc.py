#!/usr/bin/env python
"""Brain-Calc Game."""


from random import randint, choice
from operator import add, sub, mul

from brain_games.scripts.game_scripts import welcome_user, game_logic


def get_correct_answer():
    num1 = randint(1, 12)
    num2 = randint(1, 10)
    operator, op_symbol = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    print('Question: {0} {1} {2}'.format(num1, op_symbol, num2))
    result = operator(num1, num2)
    return str(result)


def main():
    """Start the "Brain-Calc Game"."""
    name = welcome_user()
    print('What is the result of the expression?')
    game_logic(name, get_correct_answer)


if __name__ == '__main__':
    main()
