#!/usr/bin/env python
"""Brain Prime Game."""


from random import randrange


from brain_games.scripts.game_scripts import welcome_user,\
    get_user_answer, is_user_answer_correct, game_messages


def get_correct_answer():
    number = randrange(1, 11)
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
