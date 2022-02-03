#!/usr/bin/env python
"""Brain Progression Game start."""


from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Start the "Brain-Progression Game"."""
    run_game(progression)


if __name__ == '__main__':
    main()
