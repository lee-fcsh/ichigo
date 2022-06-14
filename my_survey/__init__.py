#pylint: disable=import-error
"""Otree has a REST API that allows external programs to communicate with Otree,
through the following line of code: """
from otree.api import *


DOC = """
App that contains a form with two text fields to request data from users,
which will be sent with a submit button on the form
"""


class C(BaseConstants): # pylint: disable=locally-disabled, invalid-name
    """Class representing C in My Survey's experiment"""
    NAME_IN_URL = 'my_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    """Class representing a Subsession in My Survey's experiment"""

class Group(BaseGroup):
    """Class representing Group in My Survey's experiment"""

class Player(BasePlayer):
    """Class representing a Player in My Survey's experiment"""
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?')

class Survey(Page):
    """Class representing Survey in My Survey's experiment"""
    form_model = 'player'
    form_fiels = ['name', 'age']

class Results(Page):
    """Class representing last result in My Survey's experiment"""
    form_model = 'player'

page_sequence = [Survey, Results]
