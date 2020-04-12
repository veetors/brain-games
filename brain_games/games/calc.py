# -*- coding:utf-8 -*-

"""'Brain-calc' game logic."""

import random
from operator import add, mul, sub

RULES = 'What is the result of the expression?'
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_round_data():  # noqa: WPS210
    """Generate data for game.

    Returns:
        tuple: expression and current answer
    """
    operator, operation = random.choice(OPERATIONS)  # noqa: S311
    operand1 = random.randint(1, 100)  # noqa: S311
    operand2 = random.randint(1, 100)  # noqa: S311
    expression = '{num1} {operator} {num2}'.format(
        num1=operand1,
        operator=operator,
        num2=operand2,
    )
    answer = operation(operand1, operand2)

    return (expression, str(answer))
