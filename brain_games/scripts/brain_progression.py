#!/usr/bin/env python
"""Brain Progression Game start."""


from brain_games.engine import run_game
from brain_games.games.progression import make_correct_answer


def main():
    """Start the "Brain-Progression Game"."""
    run_game('progression', make_correct_answer)


if __name__ == '__main__':
    main()
