# -*- coding:utf-8 -*-

"""'Brain-progression' game logic."""

from brain_games.common import get_random_number

rules = 'What number is missing in the progression?'


def get_progression(start=1, step=1, length=10):
    """Generate arithmetic progression.

    Parameters:
        start (int): start
        step (int): step
        length (int): progression length

    Returns:
        list
    """
    progression = []
    current = start
    for index in range(length):
        current = current + step if index > 0 else current
        progression.append(current)
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
        current = '..' if index == target_index else elem
        question = '{question}{space}{current}'.format(
            question=question,
            space=space,
            current=current,
        )
    return question


def get_game_data():
    """Generate data for game.

    Returns:
        tuple
    """
    length = 10
    progression = get_progression(
        start=get_random_number(1, 10),
        step=get_random_number(1, 10),
        length=length,
    )
    target_index = get_random_number(0, length - 1)
    question = get_question(progression, target_index)
    answer = progression[target_index]

    return (question, answer)
