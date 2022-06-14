"""Module otree"""
from otree.api import *

DOC = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants): # pylint: disable=locally-disabled, invalid-name
    """Class representing C"""
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    """Class representing a Subsession"""


class Group(BaseGroup):
    """Class representing a Group"""


class Player(BasePlayer):
    """Class representing a Player______"""

# PAGES
class PaymentInfo(Page):
    """Class representing a PaymentInfo"""
    @staticmethod
    def vars_for_template(_player: Player):
        """Function to pass the redemption_code variable to the template"""
        participant = _player.participant
        return dict(redemption_code=participant.label or participant.code)


page_sequence = [PaymentInfo]
