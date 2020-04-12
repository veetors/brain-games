#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-gcd' game entry point."""

from brain_games import engine, games


def main():
    """Run 'Brain-gcd' game."""
    engine.run(games.gcd)


if __name__ == '__main__':
    main()
