#!/usr/bin/env python
"""Brain-Even Game start."""


from brain_games.engine import run_game
from brain_games.games.even import make_correct_answer


def main():
    """Start the "Brain-Even Game"."""
    run_game('even', make_correct_answer)


if __name__ == '__main__':
    main()
