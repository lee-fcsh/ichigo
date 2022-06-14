#pylint: disable=import-error
"""Otree has a REST API that allows external programs to communicate with Otree,
through the following line of code: """
from otree.api import *

DOC = """
It is an economics experiment designed to measure confidence in economic decisions.
It consists of two participants sharing a certain amount of contributions, but anonymously.
One participant can donate "x" amount of money to the other, even if they are zero contributions.
The contributions are collected by the experiment, which triples the contribution and gives
it to the other participant, even if it is zero.
"""

class C(BaseConstants): # pylint: disable=locally-disabled, invalid-name
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

class SendBack(Page):
    """Class representing a SendBack"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(_player):
        """Function that determines and shows if the page is displayed
            Args -> player: Player
            Return -> boolean

            >>> If the function determines that player.id_in_group == 2 is true,
            the page will be displayed
        """
        return _player.id_in_group == 2

    @staticmethod
    def vars_for_template(_player):
        """Function that determines the variables for the template
            Args -> player: Player
            Return -> Dictionary

            >>> The function recive 4 points, the range is from 0 to 12 points
        """
        group = _player.group
        return dict(
            tripled_amount=group.sent_amount * C.MULTIPLICATION_FACTOR
        )

# METHODS
def sent_back_amount_choices(group):
    """Function that calculates the choices for the sent back amount
        Args -> group: Group
        Return -> list of choices
        >>> The function recive 4 points, the range is from 0 to 12
    """
    return currency_range(0, group.sent_amount * C.MULTIPLICATION_FACTOR, 1)

def set_payoffs(group):
    """Function that calculates the payoffs
        Args -> group: Group
        Return -> None
        >>> This function is in charge of initializing the player 1 and player 2
            variables and the payoff attributes, respectively
    """
    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    player1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    player2.payoff = group.sent_amount * C.MULTIPLICATION_FACTOR - group.sent_back_amount

# PAGES
class Send(Page):
    """Class representing a Send"""
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(_player):
        """Function that determines and shows if the page is displayed
            Args -> player: Player
            Return -> boolean

            >>> If the function determines that player.id_in_group == 1 is true,
            the page will be displayed
        """
        return _player.id_in_group == 1

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
