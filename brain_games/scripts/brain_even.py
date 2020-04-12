#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""'Brain-even' game entry point."""

from brain_games import engine, games


def main():
    """Run 'Brain-even' game."""
    engine.run(games.even)


if __name__ == '__main__':
    main()
