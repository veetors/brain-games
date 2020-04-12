# -*- coding:utf-8 -*-

"""'Brain-gcd' game logic."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


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


def get_round_data():
    """Generate data for game.

    Returns:
        tuple
    """
    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    question = '{num1} {num2}'.format(num1=num1, num2=num2)
    greatest_common_divisor = get_greatest_common_divisor(num1, num2)
    return (question, str(greatest_common_divisor))
