"""Welcome client module."""

import prompt


def welcome_user():
    """Do greeting to user.

    Returns:
        greeting user

    """
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')
