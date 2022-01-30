#!/usr/bin/env python
"""Brain-GCD Game start."""


from brain_games.games_engine import start
from brain_games.games.gcd import TASK, make_correct_answer


def main():
    """Start the "Brain-GCD Game"."""
    start(TASK, make_correct_answer)


if __name__ == '__main__':
    main()
