"""Engine for all Brain Games."""


import prompt


def get_user_name():
    return prompt.string('May I have your name? ')


def get_user_answer():
    return prompt.string('Your answer: ')


def welcome_user():
    """Get username and greets."""
    print('Welcome to the Brain games!')
    user_name = get_user_name()
    print('Hello, {0}!'.format(user_name))
    return user_name


def is_user_answer_correct(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    return False


def game_messages(name, correct_answer, user_answer):
    messages = {
        'correct': 'Correct!',
        'win': 'Congratulations, {0}!'.format(name),
        'lost': ("'{2}' is wrong answer ;(. Correct answer was '{1}'.\n"
                 "Let\'s try again, {0}!".format(name, correct_answer,
                                                 user_answer)),
    }
    return messages


NUMBER_OF_ROUNDS = 3
FIRST_ROUND = 1


def game_logic(user_name, make_correct_answer):
    count = FIRST_ROUND
    while count <= NUMBER_OF_ROUNDS:
        correct_answer = make_correct_answer()
        user_answer = get_user_answer()
        is_user_correct = is_user_answer_correct(user_answer, correct_answer)
        game_message = game_messages(user_name, correct_answer, user_answer)
        if is_user_correct and count < NUMBER_OF_ROUNDS:
            count += 1
            print(game_message['correct'])
        elif is_user_correct and count == NUMBER_OF_ROUNDS:
            print(game_message['correct'])
            print(game_message['win'])
            break
        else:
            print(game_message['lost'])
            break


def start(TASK, make_correct_answer):
    user_name = welcome_user()
    print(TASK)
    game_logic(user_name, make_correct_answer)
