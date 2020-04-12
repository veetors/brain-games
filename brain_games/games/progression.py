# -*- coding:utf-8 -*-

"""'Brain-progression' game logic."""

import random

RULES = 'What number is missing in the progression?'


def get_progression(start, step, length):
    """Generate arithmetic progression.

    Parameters:
        start (int): start
        step (int): step
        length (int): progression length

    Returns:
        list
    """
    progression = []
    for index in range(length):
        progression.append(start + index * step)
    return progression


def get_question(iterible, target_index):
    """Create a string with a missing character from a sequence.

    Parameters:
        iterible (list): sequence
        target_index (int): index of a missing character

    Returns:
        str
    """
    question = ''
    for index, elem in enumerate(iterible):
        space = ' ' if index > 0 else ''
        current = '..' if index == target_index else str(elem)
        question += space + current
    return question


def get_round_data():
    """Generate data for game.

    Returns:
        tuple
    """
    length = 10
    progression = get_progression(
        start=random.randint(1, 10),  # noqa: S311,
        step=random.randint(1, 10),  # noqa: S311,
        length=length,
    )
    target_index = random.randint(0, length - 1)  # noqa: S311
    question = get_question(progression, target_index)
    answer = progression[target_index]

    return (question, str(answer))
