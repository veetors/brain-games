# -*- coding:utf-8 -*-

"""Brain calc game logic."""

import random
from operator import add, mul, sub

from brain_games.common import get_random_number

rules = 'What is the result of the expression?'

operators = ('+', '-', '*')
actions = {
    '+': add,
    '-': sub,
    '*': mul,
}


def get_game_data():
    """Generate data for game.

    Returns:
        tuple: expression and current answer
    """
    current_operator = random.choice(operators)  # noqa: S311
    operand1 = get_random_number()
    operand2 = get_random_number()
    expression = '{num1} {operator} {num2}'.format(
        num1=operand1,
        operator=current_operator,
        num2=operand2,
    )
    answer = actions[current_operator](operand1, operand2)

    return (expression, answer)
