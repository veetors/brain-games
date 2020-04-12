#!/usr/env/env python3
# -*- coding:utf-8 -*-

"""'Brain-progression' game entry point."""

from brain_games import engine, games


def main():
    """Run 'Brain-progression' game."""
    engine.run(games.progression)


if __name__ == '__main__':
    main()
