"""Module otree"""
from otree.api import *


DOC = """
My survey by Manuel Loor
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
