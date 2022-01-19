"""Main module of the Brain games App."""
# #!/usr/bin/env python

from brain_games.cli import welcome_user


def main():
    """Do the main start of the program."""
    print('Welcome to the Brain games!')
    print(welcome_user())


if __name__ == '__main__':
    main()
