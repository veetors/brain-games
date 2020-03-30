# -*- coding:utf-8 -*-

"""Brain even game logic."""

from brain_games.common import get_random_number

rules = 'Answer "yes" if number even otherwise answer "no".'


def get_game_data():
    """Generate data for game.

    Returns:
        tuple: random number and correct answer
    """
    number = get_random_number()
    answer = 'yes' if number % 2 == 0 else 'no'

    return (number, answer)
