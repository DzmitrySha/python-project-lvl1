"""Welcome client module."""

import prompt


def welcome_user():
    """Get name and greeting to user.

    Returns:
        greeting to user

    """
    name = prompt.string('May I have your name? ')
    return ('Hello, {0}!'.format(name))
