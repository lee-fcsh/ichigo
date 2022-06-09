"""Otree has a REST API that allows external programs to communicate with Otree,
through the following line of code: """
from otree.api import *

DOC = """
The public goods experiment is a standard of experimental economics. Participants
secretly select how many of their contributions to put into the public pot.
Contributions from this pot are multiplied by a factor, which must be greater
than 1 and less than the number of participants N, and this "public good" payment
is divided equally among the participants. Each participant will also keep the
contributions they made in the experiment.
"""

class C(BaseConstants):
    """Class representing Especial"""
    NAME_IN_URL = 'my_public_goods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(1000)
    MULTIPLIER = 2

class Subsession(BaseSubsession):
    """Class representing a Subsession"""


class Group(BaseGroup):
    """Class representing Group"""
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    """Class representing a Player"""
    contribution = models.CurrencyField(
        min = 0,
        max = C.ENDOWMENT,
        label = "How much will you contribute?"
    )

class Contribute(Page):
    """Class representing a Contribute"""
    form_model = 'player'
    form_fields = ['contribution']

# METHODS

def set_payoffs(group):
    """Function to calculate player contributions"""
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for player in players:
        player.payoff = C.ENDOWMENT - player.contribution + group.individual_share

# PAGES

class ResultsWaitPage(WaitPage):
    """Class representing ResultWaitPage"""
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """Class representing last result"""

page_sequence = [Contribute, ResultsWaitPage, Results]
