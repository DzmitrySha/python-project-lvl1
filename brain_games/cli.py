"""Welcome user script."""


import prompt


def welcome_user():
    """Get name and greeting to user.   """

    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
