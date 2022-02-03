#!/usr/bin/env python
"""Brain Prime Game start."""


from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Start the "Brain-Prime Game"."""
    run_game(prime)


if __name__ == '__main__':
    main()
