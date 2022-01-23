#!/usr/bin/env python
"""Brain Progression Game."""


from random import randrange


from brain_games.scripts.game_scripts import welcome_user,\
    get_user_answer, is_user_answer_correct, game_messages


def make_progression():
    len_progr = randrange(4, 10)
    start_num = randrange(0, 21)
    step = randrange(1, 11)
    progression = [start_num, ]
    for i in range(len_progr):
        progression.append(start_num + step)
        start_num += step
    random_index = randrange(0, len_progr + 1)
    ask_number = progression[random_index]
    progression[random_index] = '..'
    list_progr = ' '.join(map(str, progression))
    print('Question: {0}'.format(list_progr))
    return str(ask_number)


def main():
    """Start the "Brain Progression Game"."""
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 1
    while count <= 3:
        correct_answer = make_progression()
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
