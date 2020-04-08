#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""'Brain-even' game entry point."""

from brain_games.cli import run
from brain_games.games.brain_even import get_game_data, rules


def main():
    """Run 'Brain-even' game."""
    run(rules, get_game_data)


if __name__ == '__main__':
    main()
