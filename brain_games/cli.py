# -*- coding:utf-8 -*-

"""Cli functions."""

import prompt


def run(rules, get_round_data, counter=3):
    """Game engine.

    Parameters:
        rules (str): game rules
        get_round_data (callable): function that generate data for round
        counter (int, optional): number of rounds
    """
    print('Welcome to the Brain Games!')

    print(rules)

    username = prompt.string('May I have your name? ')
    print('Hello, {name}!\n'.format(name=username))

    while counter > 0:
        (question, expected_answer) = get_round_data()

        print('Question: {question}'.format(question=question))
        actual_answer = prompt.string('Your answer: ')

        if str(expected_answer) == actual_answer:
            print('Correct!')
            counter -= 1
        else:
            print(''.join((
                '"{actual}" is wrong answer ;(. '.format(
                    actual=actual_answer,
                ),
                'Correct answer was "{expected}"'.format(
                    expected=expected_answer,
                ),
            )))
            break

    print('{text}, {name}!'.format(
        text="Let's try again" if counter > 0 else 'Congratulations',
        name=username,
    ))
