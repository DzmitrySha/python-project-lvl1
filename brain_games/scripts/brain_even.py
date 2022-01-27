#!/usr/bin/env python
"""Brain-Even Game start."""


from brain_games.games_engine import start
from brain_games.games.brain_even_func import TASK, make_correct_answer


def main():
    """Start the "Brain-Even Game"."""
    start(TASK, make_correct_answer)


if __name__ == '__main__':
    main()
