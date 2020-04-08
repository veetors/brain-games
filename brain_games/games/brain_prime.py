# -*- coding:utf-8 -*-

"""'Brain-prime' game logic."""

from brain_games.common import get_random_number

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check if a number is prime.

    Parameters:
        number (int): number

    Returns:
        Bool
    """
    if number < 2:
        return False

    divider = 2
    while divider <= number / 2:
        if number % divider == 0:  # noqa: S001
            return False
        divider += 1

    return True


def get_game_data():
    """Generate data for game.

    Returns:
        tuple: random number and correct answer
    """
    number = get_random_number()
    answer = 'yes' if is_prime(number) else 'no'

    return (number, answer)
