"""Scripts for all Brain_Games Apps."""


import prompt


def welcome_user():
    """Get username and greets.

    Returns:
        - string: username

    """
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def get_user_answer():
    return prompt.string('Your answer: ')


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
