#!/usr/bin/env python
"""Brain-Calc Game start."""


from brain_games.engine import run_game
from brain_games.games.calc import TASK, make_correct_answer


def main():
    """Start the "Brain-Calc Game"."""
    run_game(TASK, make_correct_answer)


if __name__ == '__main__':
    main()
