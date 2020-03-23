# -*- coding:utf-8 -*-

"""Cli functions."""

import prompt


def welcome_user():
    """Asks for a username and greets the user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {username}!'.format(username=name))
