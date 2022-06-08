"""Module otree"""
from otree.api import *


DOC = """
My Trust by Manuel
"""


class C(BaseConstants):
    """Class representing Especial"""
    NAME_IN_URL = 'my_trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10)
    MULTIPLICATION_FACTOR = 3


class Subsession(BaseSubsession):
    """Class representing a Subsession"""


class Group(BaseGroup):
    """Class representing Group"""
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )


class Player(BasePlayer):
    """Class representing a Player"""

class Send(Page):
    """Class representing a Send"""
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player):
        """Function that shows the player that he is going to skip the page"""
        return player.id_in_group == 1

class SendBack(Page):
    """Class representing a SendBack"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player):
        """Function that shows the player that he is going to skip the page"""
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player):
        """Function to pass the tripled_amount variable to the template"""
        group = player.group
        return dict(
            tripled_amount=group.sent_amount * C.MULTIPLICATION_FACTOR
        )

# METHODS
def sent_back_amount_choices(group):
    """Function that will populate the dropdown dynamically"""
    return currency_range(
        0,
        group.sent_amount * C.MULTIPLICATION_FACTOR,
        1
    )

def set_payoffs(group):
    """Function to calculate player contributions"""
    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    player1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    player2.payoff = group.sent_amount * C.MULTIPLICATION_FACTOR - group.sent_back_amount

# PAGES

class WaitForP1(WaitPage):
    """Class representing a WaitPage"""

class ResultsWaitPage(WaitPage):
    """Class representing ResultWaitPage"""
    after_all_players_arrive = set_payoffs

class Results(Page):
    """Class representing last result"""

page_sequence = [
    Send,
    WaitForP1,
    SendBack,
    ResultsWaitPage,
    Results
]
