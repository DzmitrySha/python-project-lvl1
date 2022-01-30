#!/usr/bin/env python
"""Brain-GCD Game start."""


from brain_games.engine import run_game
from brain_games.games.gcd import make_correct_answer


def main():
    """Start the "Brain-GCD Game"."""
    run_game('gcd', make_correct_answer)


if __name__ == '__main__':
    main()
