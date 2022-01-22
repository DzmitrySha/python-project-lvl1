#!/usr/bin/env python
"""Brain-Even Game."""

from random import randint

import prompt
from brain_games.scripts.brain_games import welcome_user


def get_user_answer():
    return prompt.string('Your answer: ')


def print_game_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_number():
    number = randint(1, 99)
    print('Question: {0}'.format(number))
    return number


def make_correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game_messages(name, correct_answer, user_answer):
    game_messages = {
        'correct': 'Correct!',
        'win_answer': 'Congratulations, {0}!'.format(name),
        'lose_answer': ("'{2}' is wrong answer ;(. Correct answer was '{1}'.\n"
                        "Let\'s try again, {0}!".format(name, correct_answer, user_answer)),
    }
    return game_messages


def brain_game_logic():
    name = welcome_user()
    print_game_question()
    count = 1
    while count <= 3:
        number = get_number()
        user_answer = get_user_answer()
        correct_answer = make_correct_answer(number)
        game_message = game_messages(name, correct_answer, user_answer)
        if user_answer == correct_answer and count < 3:
            count += 1
            print(game_message['correct'])
        elif user_answer == correct_answer and count == 3:
            print(game_message['correct'])
            print(game_message['win_answer'])
            break
        else:
            print(game_message['lose_answer'])
            break


def main():
    """Do start of the "Brain-Even Game"."""
    brain_game_logic()


if __name__ == '__main__':
    main()
