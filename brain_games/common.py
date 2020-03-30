# -*- coding:utf-8 -*-

"""Common functions."""

import random


def get_random_number(start=1, stop=100):
    """Get rundom number from start to stop.

    Parameters:
        start (int): start value
        stop (int): stop value

    Returns:
        int: random number from start to stop
    """
    return random.randint(start, stop)  # noqa: S311
