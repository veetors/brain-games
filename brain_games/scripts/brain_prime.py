#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-prime' game entry point."""

from brain_games.cli import run
from brain_games.games.brain_prime import get_game_data, rules


def main():
    """Run 'Brain-prime' game."""
    run(rules, get_game_data)


if __name__ == '__main__':
    main()
