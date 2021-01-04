import logging

from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import desc
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.exc import IntegrityError

from app.models.base import Base
from app.models.base import session_scope

logger = logging.getLogger(__name__)


class User(Base):
    __tablename__ = 'M_USER'
    user_id = Column(Integer, primary_key=True, nullable=False)
    dc_uid = Column(BigInteger)
    dc_uname = Column(String(1024))

    @classmethod
    def create(cls, uid, uname):
        user = cls(dc_uid=uid,
                   dc_uname=uname)
        try:
            with session_scope() as session:
                session.add(user)
            return user
        except IntegrityError as e:
            return False

    @classmethod
    def get_by_uid(cls, uid):
        with session_scope() as session:
            user = session.query(cls).filter(
                cls.dc_uid == uid).first()
            if user is None:
                return None
            return user

    def save(self):
        with session_scope() as session:
            session.add(self)

    @classmethod
    def get_all_users(cls, limit=100):
        with session_scope() as session:
            users = session.query(cls).order_by(
                desc(cls.user_id)).limit(limit).all()

        if users is None:
            return None

        return users

    @property
    def value(self):
        return {
            'user_id': self.user_id,
            'uid': self.dc_uid,
            'uname': self.dc_uname,
        }


def update_user(uid, uname):
    user = User.get_by_uid(uid)

    if user is None:
        User.create(uid, uname)
        return False

    user.dc_uname = uname
    user.save()
    return True
