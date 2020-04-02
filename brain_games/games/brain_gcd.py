# -*- coding:utf-8 -*-

"""'Brain-gcd' game logic."""

from brain_games.common import get_random_number

rules = 'Find the greatest common divisor of given numbers.'


def get_greatest_common_divisor(num1, num2):
    """Return the greatest common divisor of two numbers.

    Parameters:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int
    """
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def get_game_data():
    """Generate data for game.

    Returns:
        tuple
    """
    num1 = get_random_number()
    num2 = get_random_number()
    question = '{num1} {num2}'.format(num1=num1, num2=num2)
    greatest_common_divisor = get_greatest_common_divisor(num1, num2)
    return (question, greatest_common_divisor)
