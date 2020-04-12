#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-prime' game entry point."""

from brain_games import engine, games


def main():
    """Run 'Brain-prime' game."""
    engine.run(games.prime)


if __name__ == '__main__':
    main()
