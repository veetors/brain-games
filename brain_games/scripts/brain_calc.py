#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-calc' game entry point."""

from brain_games import engine, games


def main():
    """Run 'Brain-calc' game."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()
