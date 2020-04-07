#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-progression' game entry point."""

from brain_games.cli import run
from brain_games.games.brain_progression import get_game_data, rules


def main():
    """Run 'Brain-progression' game."""
    run(rules, get_game_data)


if __name__ == '__main__':
    main()
