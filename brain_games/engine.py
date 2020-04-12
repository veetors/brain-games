# -*- coding:utf-8 -*-

"""Game engine module."""

import prompt


def run(game, counter=3):
    """Game engine.

    Parameters:
        game(module): module with game.
        counter (int, optional): number of rounds
    """
    print('Welcome to the Brain Games!')

    print(game.RULES)

    username = prompt.string('May I have your name? ')
    print('Hello, {name}!\n'.format(name=username))

    while counter > 0:
        question, expected_answer = game.get_round_data()

        print('Question: {question}'.format(question=question))
        actual_answer = prompt.string('Your answer: ')

        if expected_answer != actual_answer:
            print((
                '"{actual}" is wrong answer ;(. '
                'Correct answer was "{expected}"\n'  # noqa: WPS326
                "Let's try again, {name}!"  # noqa: WPS326
            ).format(
                actual=actual_answer,
                expected=expected_answer,
                name=username,
            ))

            return

        print('Correct!\nCongratulations, {name}!'.format(name=username))
        counter -= 1
