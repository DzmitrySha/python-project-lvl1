#!/usr/bin/env python
"""Brain-Calc Game start."""


from brain_games.games_engine import start
from brain_games.games.brain_calc_func import TASK, make_correct_answer


def main():
    """Start the "Brain-Calc Game"."""
    start(TASK, make_correct_answer)


if __name__ == '__main__':
    main()
