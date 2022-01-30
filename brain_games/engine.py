"""Engine for all Brain Games."""

import prompt

MAX_ROUNDS = 3

GAMES_QUESTIONS = {
    'calc': 'What is the result of the expression?',
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'prime': "Answer 'yes' if given number is prime. Otherwise answer 'no'.",
    'progression': 'What number is missing in the progression?',
}


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


def run_game(game_name, make_correct_answer):
    user_name = welcome_user()
    print(GAMES_QUESTIONS[game_name])
    round_number = 1
    while round_number <= MAX_ROUNDS:
        correct_answer = make_correct_answer()
        user_answer = prompt.string('Your answer: ')
        game_message = make_messages(user_name, correct_answer, user_answer)
        if not is_user_answer_correct(user_answer, correct_answer):
            print(game_message['lost'])
            break
        print(game_message['correct'])
        round_number += 1
    else:
        print(game_message['win'])
