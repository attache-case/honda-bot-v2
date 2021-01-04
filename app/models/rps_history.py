from datetime import datetime
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


class RpsHistory(Base):
    __tablename__ = 'T_RPS_HISTORY'

    rps_history_id = Column(Integer, primary_key=True, nullable=False)
    dc_uid = Column(BigInteger)
    hand = Column(Integer)
    result = Column(Integer)
    created_at = Column(DateTime)

    @classmethod
    def create(cls, uid, hand: Hand, result: Result):
        rps_history = cls(dc_uid=uid,
                          hand=hand.value,
                          result=result.value,
                          created_at=datetime.utcnow())
        try:
            with session_scope() as session:
                session.add(rps_history)
            return rps_history
        except IntegrityError as e:
            return False

    @classmethod
    def get_last_history(cls, uid):
        with session_scope() as session:
            rps_history = session.query(cls).filter(
                cls.dc_uid == uid).order_by(desc(cls.created_at)).limit(1).all()

        if not rps_history:
            return None

        return rps_history[0]

    @property
    def value(self):
        return {
            'rps_history_id': self.rps_history_id,
            'uid': self.dc_uid,
            'hand': Hand(self.hand),
            'result': Result(self.result),
            'created_at': self.created_at
        }
