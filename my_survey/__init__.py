"""Otree has a REST API that allows external programs to communicate with Otree,
through the following line of code: """
from otree.api import *


DOC = """
App that contains a form with two text fields to request data from users,
which will be sent with a submit button on the form
"""


class C(BaseConstants):
    """Class representing Especial"""
    NAME_IN_URL = 'my_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    """Class representing a Subsession"""

class Group(BaseGroup):
    """Class representing Group"""

class Player(BasePlayer):
    """Class representing a Player"""
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?')

class Survey(Page):
    """Class representing Survey"""
    form_model = 'player'
    form_fiels = ['name', 'age']

class Results(Page):
    """Class representing last result"""
    form_model = 'player'

page_sequence = [Survey, Results]
