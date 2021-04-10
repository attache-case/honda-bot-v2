import settings
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import threading
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
Base = declarative_base()
engine = create_engine(
    f'{settings.db_url}?charset=utf8&sslmode=require', echo=True)
Session = scoped_session(sessionmaker(bind=engine))
lock = threading.Lock()


@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        lock.acquire()
        yield session
        session.commit()
    except Exception as e:
        logger.error(f'action=session_scope error={e}')
        session.rollback()
        raise
    finally:
        session.expire_on_commit = True
        lock.release()
        session.close()


def init_db():
    import app.models.user
    import app.models.rps_history
    import app.models.rps_stat
    Base.metadata.create_all(bind=engine)
