#!/usr/bin/env python
"""Brain-GCD Game."""


from random import randint
from math import gcd

from brain_games.scripts.game_scripts import welcome_user,\
    get_user_answer, is_user_answer_correct, game_messages


def make_expression():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    print('Question: {0} {1}'.format(num1, num2))
    correct_answer = gcd(num1, num2)
    return str(correct_answer)


def main():
    """Start the "Brain-GCD Game"."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
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
