#!/usr/bin/env python
"""Brain Progression Game start."""


from brain_games.games_engine import start
from brain_games.games.brain_progression_func import TASK, make_correct_answer


def main():
    """Start the "Brain-Progression Game"."""
    start(TASK, make_correct_answer)


if __name__ == '__main__':
    main()
