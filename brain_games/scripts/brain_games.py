#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Package entry point."""

from brain_games import cli


def main():
    """Run main script."""
    print('Welcome to the Brain Games!')

    cli.welcome_user()


if __name__ == '__main__':
    main()
