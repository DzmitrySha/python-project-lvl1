#!/usr/bin/env python
"""Welcome user script."""


import prompt


def welcome_user():
    """Get name and greeting to user.   """

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    welcome_user()
