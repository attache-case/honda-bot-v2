import logging

from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import desc
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.exc import IntegrityError

from app.models.base import Base
from app.models.base import session_scope
from app.models.enum_rps import Hand, Result

logger = logging.getLogger(__name__)


class RpsStat(Base):
    __tablename__ = 'T_RPS_STAT'

    rps_stat_id = Column(Integer, primary_key=True, nullable=False)
    dc_uid = Column(BigInteger)
    hand_rock_cnt = Column(Integer)
    hand_paper_cnt = Column(Integer)
    hand_scissors_cnt = Column(Integer)
    result_win_cnt = Column(Integer)
    result_lose_cnt = Column(Integer)
    result_draw_cnt = Column(Integer)
    continuous_win_cnt = Column(Integer)
    continuous_lose_cnt = Column(Integer)
    continuous_login_cnt = Column(Integer)
    last_battle_at = Column(DateTime)

    @classmethod
    def create(cls, uid):
        rps_stat = cls(dc_uid=uid,
                       hand_rock_cnt=0,
                       hand_paper_cnt=0,
                       hand_scissors_cnt=0,
                       result_win_cnt=0,
                       result_lose_cnt=0,
                       result_draw_cnt=0,
                       continuous_win_cnt=0,
                       continuous_lose_cnt=0,
                       continuous_login_cnt=0)
        try:
            with session_scope() as session:
                session.add(rps_stat)
            return rps_stat
        except IntegrityError as e:
            return False

    @classmethod
    def get_by_uid(cls, uid):
        with session_scope() as session:
            rps_stat = session.query(cls).filter(
                cls.dc_uid == uid).first()
            if rps_stat is None:
                return None
            return rps_stat

    def save(self):
        with session_scope() as session:
            session.add(self)

    def update_info(self, hand: Hand, result: Result, current_battle_time):
        if hand == Hand.ROCK:
            self.hand_rock_cnt += 1
        elif hand == Hand.PAPER:
            self.hand_paper_cnt += 1
        elif hand == Hand.SCISSORS:
            self.hand_scissors_cnt += 1
        if result == Result.WIN:
            self.result_win_cnt += 1
            self.continuous_win_cnt += 1
            self.continuous_lose_cnt = 0
        elif result == Result.LOSE:
            self.result_lose_cnt += 1
            self.continuous_lose_cnt += 1
            self.continuous_win_cnt = 0
        elif result == Result.DRAW:
            self.result_draw_cnt += 1

        if self.last_battle_at is not None:
            td_from_last_battle = current_battle_time - self.last_battle_at
            if td_from_last_battle.day == 0:
                self.continuous_login_cnt += 1
            else:
                self.continuous_login_cnt = 1
        else:
            self.continuous_login_cnt = 1
        self.last_battle_at = current_battle_time

    @classmethod
    def get_all_rps_stats(cls, limit=100):
        with session_scope() as session:
            rps_stats = session.query(cls).order_by(
                desc(cls.rps_stat_id)).limit(limit).all()

        if rps_stats is None:
            return None

        return rps_stats

    @property
    def value(self):
        return {
            'rps_stat_id': self.rps_stat_id,
            'uid': self.dc_uid,
            'hand_rock_cnt': self.hand_rock_cnt,
            'hand_paper_cnt': self.hand_paper_cnt,
            'hand_scissors_cnt': self.hand_scissors_cnt,
            'result_win_cnt': self.result_win_cnt,
            'result_lose_cnt': self.result_lose_cnt,
            'result_draw_cnt': self.result_draw_cnt,
            'continuous_win_cnt': self.continuous_win_cnt,
            'continuous_lose_cnt': self.continuous_lose_cnt,
            'continuous_login_cnt': self.continuous_login_cnt,
            'last_battle_at': self.last_battle_at
        }


def update_rps_stat(uid, hand: Hand, result: Result, current_battle_time):
    rps_stat = RpsStat.get_by_uid(uid)

    if rps_stat is None:
        rps_stat = RpsStat.create(uid)

    rps_stat.update_info(hand, result, current_battle_time)
    rps_stat.save()
    return True
