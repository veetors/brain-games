# -*- coding:utf-8 -*-

"""Brain even game logic."""

import random

rules = 'Answer "yes" if number even otherwise answer "no".'


def get_game_data():
    """Generate data for game.

    Returns:
        tuple: random number and correct answer
    """
    number = random.randint(1, 100)  # noqa: S311
    answer = 'yes' if number % 2 == 0 else 'no'

    return (number, answer)
