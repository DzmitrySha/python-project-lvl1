#!/usr/bin/env python
"""Brain-Even Game."""


from random import randint

from brain_games.scripts.game_scripts import welcome_user, \
    get_user_answer, game_messages, is_user_answer_correct


def get_correct_answer():
    number = randint(1, 99)
    print('Question: {0}'.format(number))
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    """Start the "Brain-Even Game"."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        correct_answer = get_correct_answer()
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
