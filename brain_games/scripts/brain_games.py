#!/usr/bin/env python
"""Main module of the Brain games App."""


import prompt


def welcome_user():
    """Get user name and greets.

    Returns:
        - string: name of user

    """
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def main():
    welcome_user()


if __name__ == '__main__':
    main()
