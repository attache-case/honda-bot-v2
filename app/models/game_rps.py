import logging
import random

from app.models.enum_rps import Hand, Result
from app.models.rps_history import RpsHistory
from utils.utils import get_prev_refresh_utc, has_keyword

import constants
import settings

logger = logging.getLogger(__name__)


HAND_KEYWORDS_MAP = {
    Hand.ROCK: constants.HAND_R_KEYWORDS,
    Hand.PAPER: constants.HAND_P_KEYWORDS,
    Hand.SCISSORS: constants.HAND_S_KEYWORDS
}

HAND_EMOJI_MAP = {
    Hand.ROCK: constants.DISCORD_EMOJI_R,
    Hand.PAPER: constants.DISCORD_EMOJI_P,
    Hand.SCISSORS: constants.DISCORD_EMOJI_S
}

HAND_MAP = {
    Hand.ROCK: {
        Result.WIN: Hand.SCISSORS,
        Result.LOSE: Hand.PAPER,
        Result.DRAW: Hand.ROCK
    },
    Hand.PAPER: {
        Result.WIN: Hand.ROCK,
        Result.LOSE: Hand.SCISSORS,
        Result.DRAW: Hand.PAPER
    },
    Hand.SCISSORS: {
        Result.WIN: Hand.PAPER,
        Result.LOSE: Hand.ROCK,
        Result.DRAW: Hand.SCISSORS
    }
}


class GameRPS(object):

    def __init__(self):
        pass

    @classmethod
    def has_played_today(cls, uid):
        rps_history = RpsHistory.get_last_history(uid)
        if rps_history is None:
            return False
        if rps_history.created_at >= get_prev_refresh_utc():
            return True
        else:
            return False

    @classmethod
    def parse_hands(cls, text):
        hands = Hand(0)
        for hand in Hand:
            if has_keyword(text, HAND_KEYWORDS_MAP[hand]):
                hands = hands | hand
        return hands

    @classmethod
    def is_valid_hand(cls, hands: Hand):
        return any([hand == hands for hand in Hand])

    @classmethod
    def create_rps_battle_string(cls, hand: Hand, result: Result, player_name='YOU', opponent_name='OPPONENT'):
        a = HAND_EMOJI_MAP[hand]
        b = HAND_EMOJI_MAP[HAND_MAP[hand][result]]
        return f'({player_name}) {a} VS {b} ({opponent_name})'

    @classmethod
    def decide_result(cls) -> Result:
        rnd = random.random()
        if rnd < settings.win_rate:
            return Result.WIN
        else:
            return Result.LOSE
