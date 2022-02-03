"""Engine for all Brain Games."""

import prompt
from random import randint

MAX_ROUNDS = 3

GAMES_DESCRIPTIONS = {
    'brain_games.games.calc': 'What is the result of the expression?',
    'brain_games.games.even': 'Answer "yes" if the number is even, '
                              'otherwise answer "no".',
    'brain_games.games.gcd': 'Find the greatest common divisor of given '
                             'numbers.',
    'brain_games.games.prime': 'Answer "yes" if given number is prime. '
                               'Otherwise answer "no".',
    'brain_games.games.progression': 'What number is missing in the '
                                     'progression?',
}


def get_description(game_name):
    name = str(game_name.__name__)
    if name in GAMES_DESCRIPTIONS.keys():
        game_description = GAMES_DESCRIPTIONS[name]
        return game_description


def generate_number(min_number=1, max_number=99):
    return randint(min_number, max_number)


def welcome_user():
    """Get username and greets."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def is_user_answer_correct(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    return False


def make_messages(user_name, correct_answer, user_answer):
    messages = {
        'correct': "Correct!",
        'win': f"Congratulations, {user_name}!",
        'lost': (f"'{user_answer}' is wrong answer ;(. "
                 f"Correct answer was '{correct_answer}'.\n"
                 f"Let\'s try again, {user_name}!"),
    }
    return messages


def run_game(game_name):
    user_name = welcome_user()
    print(get_description(game_name))
    round_number = 1
    while round_number <= MAX_ROUNDS:
        correct_answer, question = game_name.make_correct_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        game_message = make_messages(user_name, correct_answer, user_answer)
        if not is_user_answer_correct(user_answer, correct_answer):
            print(game_message['lost'])
            break
        print(game_message['correct'])
        round_number += 1
    else:
        print(game_message['win'])
