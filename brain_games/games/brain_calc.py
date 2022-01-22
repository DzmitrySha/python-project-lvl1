#!/usr/bin/env python
"""Brain-Calc Game."""


from random import randint, choice
from operator import add, sub, mul

from brain_games.scripts.game_scripts import welcome_user,\
    get_user_answer, is_user_answer_correct, game_messages


def make_expression():
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
    count = 1
    while count <= 3:
        correct_answer = make_expression()
        user_answer = get_user_answer()
        user_correct = is_user_answer_correct(user_answer, correct_answer)
        game_message = game_messages(name, correct_answer, user_answer)
        if user_correct and count < 3:
            count += 1
            print(game_message['correct'])
        elif user_correct and count == 3:
            print(game_message['correct'])
            print(game_message['win'])
            break
        else:
            print(game_message['lost'])
            break


if __name__ == '__main__':
    main()
