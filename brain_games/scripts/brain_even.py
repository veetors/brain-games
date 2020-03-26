#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Brain even game entry point."""

from brain_games.brain_even import get_game_data, rules
from brain_games.cli import run


def main():
    """Run 'Brain even' game."""
    run(rules, get_game_data)


if __name__ == '__main__':
    main()
